.PHONY: install clean all install-ordered build install-wheels check-deps wsl

# Detect OS for platform-specific commands
ifeq ($(OS),Windows_NT)
    # Windows-specific settings
    MKDIR = if not exist dist mkdir dist
    RM_CMD = powershell -Command "Remove-Item -Recurse -Force"
    IS_WINDOWS = 1
else
    # Linux/Mac-specific settings
    MKDIR = mkdir -p dist
    RM_CMD = rm -rf
    IS_WINDOWS = 0
    # Check if running under WSL
    ifeq ($(shell uname -a | grep -i microsoft),)
        IS_WSL = 0
    else
        IS_WSL = 1
    endif
endif

# Default target
all: install-ordered

# Check for required dependencies
check-deps:
	@echo "Checking for required dependencies..."
ifeq ($(IS_WINDOWS),1)
	@powershell -Command " \
		$$missing = @(); \
		if (-not (Get-Command python -ErrorAction SilentlyContinue)) { $$missing += 'python'; } \
		try { \
			$$buildModule = python -c \"import importlib.util; print('True' if importlib.util.find_spec('build') else 'False')\" 2>$$null; \
			if ($$buildModule -ne 'True') { $$missing += 'build'; } \
		} catch { \
			$$missing += 'build'; \
		} \
		try { \
			$$pipModule = python -c \"import importlib.util; print('True' if importlib.util.find_spec('pip') else 'False')\" 2>$$null; \
			if ($$pipModule -ne 'True') { $$missing += 'pip'; } \
		} catch { \
			$$missing += 'pip'; \
		} \
		if ($$missing.Count -gt 0) { \
			Write-Host \"Missing dependencies: $$missing\" -ForegroundColor Red; \
			Write-Host \"Please install them with: python -m pip install build\" -ForegroundColor Yellow; \
			exit 1; \
		} else { \
			Write-Host \"All dependencies found!\" -ForegroundColor Green; \
		} \
	"
else
	@missing_deps="" ; \
	command -v python3 >/dev/null 2>&1 || missing_deps="$$missing_deps python3" ; \
	python3 -c "import build" >/dev/null 2>&1 || missing_deps="$$missing_deps build" ; \
	command -v pip3 >/dev/null 2>&1 || missing_deps="$$missing_deps pip3" ; \
	if [ ! -z "$$missing_deps" ]; then \
		echo "Missing dependencies:$$missing_deps" ; \
		echo "Please install them with: python3 -m pip install build" ; \
		exit 1 ; \
	else \
		echo "All dependencies found!" ; \
	fi
endif

# Installation order - libraries listed in dependency order
INSTALL_ORDER = libraries/Core/microsoft-agents-core \
                libraries/Core/microsoft-agents-authorization \
                libraries/Authentication/microsoft-agents-authentication-msal \
                libraries/Storage/microsoft-agents-storage \
                libraries/Client/microsoft-agents-connector \
                libraries/Client/microsoft-agents-client \
                libraries/Client/microsoft-agents-copilotstudio-client \
                libraries/Builder/microsoft-agents-builder \
                libraries/Hosting/microsoft-agents-hosting-aiohttp

# Install packages in dependency order
install-ordered: check-deps
	@$(MKDIR)
	@echo "Installing packages in specified dependency order..."
ifeq ($(IS_WINDOWS),1)
	@powershell -Command " \
		$$ErrorActionPreference = 'Continue'; \
		$$packages = @( \
			'libraries/Core/microsoft-agents-core', \
			'libraries/Core/microsoft-agents-authorization', \
			'libraries/Authentication/microsoft-agents-authentication-msal', \
			'libraries/Storage/microsoft-agents-storage', \
			'libraries/Client/microsoft-agents-connector', \
			'libraries/Client/microsoft-agents-client', \
			'libraries/Client/microsoft-agents-copilotstudio-client', \
			'libraries/Builder/microsoft-agents-builder', \
			'libraries/Hosting/microsoft-agents-hosting-aiohttp' \
		); \
		$$failed = @(); \
		foreach ($$pkg in $$packages) { \
			Write-Host \"Installing $$pkg in development mode...\"; \
			Push-Location $$pkg; \
			pip install -e .; \
			if ($$LASTEXITCODE -ne 0) { \
				Write-Host \"Warning: Installation may have issues for $$pkg\" -ForegroundColor Yellow; \
				$$failed += $$pkg; \
			} \
			Pop-Location; \
		} \
		if ($$failed.Count -gt 0) { \
			Write-Host \"The following packages had installation issues:\" -ForegroundColor Yellow; \
			$$failed | ForEach-Object { Write-Host \"  - $$_\" -ForegroundColor Yellow }; \
		} else { \
			Write-Host \"All packages installed successfully!\" -ForegroundColor Green; \
		} \
	"
else
	@for pkg in $(INSTALL_ORDER); do \
		echo "Installing $$pkg in development mode..."; \
		(cd $$pkg && python3 -m pip install -e .); \
	done
endif
	@echo "Installation process completed!"

# Original install target - installs all without specific ordering
install: check-deps
	@$(MKDIR)
	@echo "Installing all packages in development mode (without specific ordering)..."
ifeq ($(IS_WINDOWS),1)
	@powershell -Command "Get-ChildItem -Path libraries -Recurse -Filter 'pyproject.toml' | ForEach-Object { $$dir = $$_.Directory; Write-Host \"Installing $$($$(Split-Path -Leaf $$dir)) in development mode...\"; Push-Location $$dir; pip install -e .; Pop-Location }"
else
	@find libraries -mindepth 2 -maxdepth 2 -type f -name pyproject.toml | while read file; do \
		dir=$$(dirname $$file); \
		echo "Installing $$(basename $$dir) in development mode..."; \
		(cd $$dir && python3 -m pip install -e .); \
	done
endif
	@echo "All packages installed in development mode successfully!"

# Build wheel packages
build: check-deps
	@$(MKDIR)
	@echo "Building wheel packages for all libraries..."
ifeq ($(IS_WINDOWS),1)
	@powershell -Command " \
		Get-ChildItem -Path libraries -Directory | ForEach-Object { \
			$$category = $$_.FullName; \
			Get-ChildItem -Path $$category -Directory | ForEach-Object { \
				$$pkg = $$_.FullName; \
				if (Test-Path \"$$pkg\\pyproject.toml\") { \
					Write-Host \"Building $$(Split-Path -Leaf $$pkg) package...\"; \
					Push-Location $$pkg; \
					python -m build --outdir ..\\..\\..\dist; \
					Pop-Location; \
				} \
			} \
		} \
	"
else
	@for dir in libraries/*; do \
		if [ -d "$$dir" ]; then \
			for subdir in "$$dir"/*; do \
				if [ -f "$$subdir/pyproject.toml" ]; then \
					echo "Building $$(basename $$subdir) package..."; \
					(cd "$$subdir" && python3 -m build --outdir ../../../dist); \
				fi \
			done \
		fi \
	done
endif
	@echo "All packages built successfully!"

# Install wheel packages
install-wheels: build
	@echo "Installing wheel packages from dist directory..."
ifeq ($(IS_WINDOWS),1)
	@powershell -Command " \
		$$ErrorActionPreference = 'Continue'; \
		$$packages = @(); \
		Get-ChildItem -Path './dist' -Filter \"*.whl\" | Sort-Object -Property LastWriteTime -Descending | ForEach-Object { $$packages += $$_.FullName }; \
		if ($$packages.Count -gt 0) { \
			Write-Host \"Installing all wheel packages in one command to resolve dependencies...\"; \
			pip install --force-reinstall $$packages; \
			if ($$LASTEXITCODE -ne 0) { \
				Write-Host \"Warning: Some packages may not have installed correctly\" -ForegroundColor Yellow; \
				exit 1; \
			} else { \
				Write-Host \"All packages installed successfully!\" -ForegroundColor Green; \
			} \
		} else { \
			Write-Host \"No wheel files found in the dist directory!\" -ForegroundColor Red; \
			exit 1; \
		} \
	"
else
	@echo "Installing all wheel packages together to resolve dependencies..."
	@wheel_files=$$(find ./dist -name "*.whl" | tr '\n' ' '); \
	if [ ! -z "$$wheel_files" ]; then \
		python3 -m pip install --force-reinstall $$wheel_files || echo "Warning: Some packages may not have installed correctly"; \
	else \
		echo "No wheel files found in the dist directory!"; \
		exit 1; \
	fi
endif
	@echo "All wheel packages installed successfully!"

# Special target for WSL - handles path conversion and other WSL-specific considerations
wsl: check-deps
	@echo "Running WSL-specific setup..."
ifeq ($(IS_WSL),1)
	@echo "WSL environment detected, using appropriate path conversions..."
	@mkdir -p dist
	@for dir in libraries/*; do \
		if [ -d "$$dir" ]; then \
			for subdir in "$$dir"/*; do \
				if [ -f "$$subdir/pyproject.toml" ]; then \
					echo "Building $$(basename $$subdir) package..."; \
					(cd "$$subdir" && python3 -m build --outdir ../../../dist); \
				fi \
			done \
		fi \
	done
	@echo "Installing wheel packages from dist directory..."
	@echo "Installing all wheel packages together to resolve dependencies..."
	@wheel_files=$$(find ./dist -name "*.whl" | tr '\n' ' '); \
	if [ ! -z "$$wheel_files" ]; then \
		python3 -m pip install --force-reinstall $$wheel_files || echo "Warning: Some packages may not have installed correctly"; \
	else \
		echo "No wheel files found in the dist directory!"; \
		exit 1; \
	fi
	@echo "WSL setup completed!"
else
	@echo "Not running in WSL. Please use 'make install-wheels' instead."
endif

# Clean up build artifacts
clean:
	@echo "Cleaning up build artifacts..."
ifeq ($(IS_WINDOWS),1)
	@powershell -Command "Get-ChildItem -Path . -Recurse -Include '*.egg-info','__pycache__' -Directory | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue"
	@powershell -Command "Get-ChildItem -Path . -Recurse -Include '*.pyc' -File | Remove-Item -Force -ErrorAction SilentlyContinue"
	@powershell -Command "if (Test-Path dist) { Remove-Item -Recurse -Force dist }"
else
	@find . -name "*.egg-info" -type d -exec $(RM_CMD) {} +
	@find . -name "__pycache__" -type d -exec $(RM_CMD) {} +
	@find . -name "*.pyc" -type f -delete
	@if [ -d dist ]; then $(RM_CMD) dist; fi
endif
	@echo "Cleanup complete!"

# Define necessary variables for Windows command interpretation
COMMA := ,
SPACE := $(null) $(null)