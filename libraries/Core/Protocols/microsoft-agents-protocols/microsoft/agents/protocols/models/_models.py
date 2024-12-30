# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from datetime import datetime, timezone
from enum import Enum
from pydantic import BaseModel, Field


class ActivityEventNames(str, Enum):
    continue_conversation = "ContinueConversation"
    create_conversation = "CreateConversation"


class ConversationReference(BaseModel):
    """An object relating to a particular point in a conversation.

    :param activity_id: (Optional) ID of the activity to refer to
    :type activity_id: str
    :param user: (Optional) User participating in this conversation
    :type user: ~microsoft.agents.protocols.models.ChannelAccount
    :param bot: Bot participating in this conversation
    :type bot: ~microsoft.agents.protocols.models.ChannelAccount
    :param conversation: Conversation reference
    :type conversation: ~microsoft.agents.protocols.models.ConversationAccount
    :param channel_id: Channel ID
    :type channel_id: str
    :param locale: A locale name for the contents of the text field.
        The locale name is a combination of an ISO 639 two- or three-letter
        culture code associated with a language and an ISO 3166 two-letter
        subculture code associated with a country or region.
        The locale name can also correspond to a valid BCP-47 language tag.
    :type locale: str
    :param service_url: Service endpoint where operations concerning the
     referenced conversation may be performed
    :type service_url: str
    """

    activity_id: str = Field(None, alias="activityId")
    user: ChannelAccount = Field(None, alias="user")
    bot: ChannelAccount = Field(None, alias="bot")
    conversation: ConversationAccount = Field(None, alias="conversation")
    channel_id: str = Field(None, alias="channelId")
    locale: str = Field(None, alias="locale")
    service_url: str = Field(None, alias="serviceUrl")

    def __init__(
        self,
        *,
        activity_id: str = None,
        user=None,
        bot=None,
        conversation=None,
        channel_id: str = None,
        locale: str = None,
        service_url: str = None,
        **kwargs
    ) -> None:
        super(ConversationReference, self).__init__(**kwargs)
        self.activity_id = activity_id
        self.user = user
        self.bot = bot
        self.conversation = conversation
        self.channel_id = channel_id
        self.locale = locale
        self.service_url = service_url


class Mention(BaseModel):
    """Mention information (entity type: "mention").

    :param mentioned: The mentioned user
    :type mentioned: ~microsoft.agents.protocols.models.ChannelAccount
    :param text: Sub Text which represents the mention (can be null or empty)
    :type text: str
    :param type: Type of this entity (RFC 3987 IRI)
    :type type: str
    """

    mentioned: ChannelAccount = Field(None, alias="mentioned")
    text: str = Field(None, alias="text")
    type: str = Field(None, alias="type")

    def __init__(
        self, *, mentioned=None, text: str = None, type: str = None, **kwargs
    ) -> None:
        super(Mention, self).__init__(**kwargs)
        self.mentioned = mentioned
        self.text = text
        self.type = type


class ResourceResponse(BaseModel):
    """A response containing a resource ID.

    :param id: Id of the resource
    :type id: str
    """

    id: str = Field(None, alias="id")

    def __init__(self, *, id: str = None, **kwargs) -> None:
        super(ResourceResponse, self).__init__(**kwargs)
        self.id = id


class Activity(BaseModel):
    """An Activity is the basic communication type for the Bot Framework 3.0
    protocol.

    :param type: Contains the activity type. Possible values include:
     'message', 'contactRelationUpdate', 'conversationUpdate', 'typing',
     'endOfConversation', 'event', 'invoke', 'deleteUserData', 'messageUpdate',
     'messageDelete', 'installationUpdate', 'messageReaction', 'suggestion',
     'trace', 'handoff'
    :type type: str or ~microsoft.agents.protocols.models.ActivityTypes
    :param id: Contains an ID that uniquely identifies the activity on the
     channel.
    :type id: str
    :param timestamp: Contains the date and time that the message was sent, in
     UTC, expressed in ISO-8601 format.
    :type timestamp: datetime
    :param local_timestamp: Contains the local date and time of the message
     expressed in ISO-8601 format.
     For example, 2016-09-23T13:07:49.4714686-07:00.
    :type local_timestamp: datetime
    :param local_timezone: Contains the name of the local timezone of the message,
     expressed in IANA Time Zone database format.
     For example, America/Los_Angeles.
    :type local_timezone: str
    :param service_url: Contains the URL that specifies the channel's service
     endpoint. Set by the channel.
    :type service_url: str
    :param channel_id: Contains an ID that uniquely identifies the channel.
     Set by the channel.
    :type channel_id: str
    :param from_property: Identifies the sender of the message.
    :type from_property: ~microsoft.agents.protocols.models.ChannelAccount
    :param conversation: Identifies the conversation to which the activity
     belongs.
    :type conversation: ~microsoft.agents.protocols.models.ConversationAccount
    :param recipient: Identifies the recipient of the message.
    :type recipient: ~microsoft.agents.protocols.models.ChannelAccount
    :param text_format: Format of text fields Default:markdown. Possible
     values include: 'markdown', 'plain', 'xml'
    :type text_format: str or ~microsoft.agents.protocols.models.TextFormatTypes
    :param attachment_layout: The layout hint for multiple attachments.
     Default: list. Possible values include: 'list', 'carousel'
    :type attachment_layout: str or
     ~microsoft.agents.protocols.models.AttachmentLayoutTypes
    :param members_added: The collection of members added to the conversation.
    :type members_added: list[~microsoft.agents.protocols.models.ChannelAccount]
    :param members_removed: The collection of members removed from the
     conversation.
    :type members_removed: list[~microsoft.agents.protocols.models.ChannelAccount]
    :param reactions_added: The collection of reactions added to the
     conversation.
    :type reactions_added:
     list[~microsoft.agents.protocols.models.MessageReaction]
    :param reactions_removed: The collection of reactions removed from the
     conversation.
    :type reactions_removed:
     list[~microsoft.agents.protocols.models.MessageReaction]
    :param topic_name: The updated topic name of the conversation.
    :type topic_name: str
    :param history_disclosed: Indicates whether the prior history of the
     channel is disclosed.
    :type history_disclosed: bool
    :param locale: A locale name for the contents of the text field.
     The locale name is a combination of an ISO 639 two- or three-letter
     culture code associated with a language
     and an ISO 3166 two-letter subculture code associated with a country or
     region.
     The locale name can also correspond to a valid BCP-47 language tag.
    :type locale: str
    :param text: The text content of the message.
    :type text: str
    :param speak: The text to speak.
    :type speak: str
    :param input_hint: Indicates whether your bot is accepting,
     expecting, or ignoring user input after the message is delivered to the
     client. Possible values include: 'acceptingInput', 'ignoringInput',
     'expectingInput'
    :type input_hint: str or ~microsoft.agents.protocols.models.InputHints
    :param summary: The text to display if the channel cannot render cards.
    :type summary: str
    :param suggested_actions: The suggested actions for the activity.
    :type suggested_actions: ~microsoft.agents.protocols.models.SuggestedActions
    :param attachments: Attachments
    :type attachments: list[~microsoft.agents.protocols.models.Attachment]
    :param entities: Represents the entities that were mentioned in the
     message.
    :type entities: list[~microsoft.agents.protocols.models.Entity]
    :param channel_data: Contains channel-specific content.
    :type channel_data: object
    :param action: Indicates whether the recipient of a contactRelationUpdate
     was added or removed from the sender's contact list.
    :type action: str
    :param reply_to_id: Contains the ID of the message to which this message
     is a reply.
    :type reply_to_id: str
    :param label: A descriptive label for the activity.
    :type label: str
    :param value_type: The type of the activity's value object.
    :type value_type: str
    :param value: A value that is associated with the activity.
    :type value: object
    :param name: The name of the operation associated with an invoke or event
     activity.
    :type name: str
    :param relates_to: A reference to another conversation or activity.
    :type relates_to: ~microsoft.agents.protocols.models.ConversationReference
    :param code: The a code for endOfConversation activities that indicates
     why the conversation ended. Possible values include: 'unknown',
     'completedSuccessfully', 'userCancelled', 'botTimedOut',
     'botIssuedInvalidMessage', 'channelFailed'
    :type code: str or ~microsoft.agents.protocols.models.EndOfConversationCodes
    :param expiration: The time at which the activity should be considered to
     be "expired" and should not be presented to the recipient.
    :type expiration: datetime
    :param importance: The importance of the activity. Possible values
     include: 'low', 'normal', 'high'
    :type importance: str or ~microsoft.agents.protocols.models.ActivityImportance
    :param delivery_mode: A delivery hint to signal to the recipient alternate
     delivery paths for the activity.
     The default delivery mode is "default". Possible values include: 'normal',
     'notification', 'expectReplies', 'ephemeral'
    :type delivery_mode: str or ~microsoft.agents.protocols.models.DeliveryModes
    :param listen_for: List of phrases and references that speech and language
     priming systems should listen for
    :type listen_for: list[str]
    :param text_highlights: The collection of text fragments to highlight when
     the activity contains a ReplyToId value.
    :type text_highlights: list[~microsoft.agents.protocols.models.TextHighlight]
    :param semantic_action: An optional programmatic action accompanying this
     request
    :type semantic_action: ~microsoft.agents.protocols.models.SemanticAction
    :param caller_id: A string containing an IRI identifying the caller of a
     bot. This field is not intended to be transmitted over the wire, but is
     instead populated by bots and clients based on cryptographically
     verifiable data that asserts the identity of the callers (e.g. tokens).
    :type caller_id: str
    """

    type: str = Field(None, alias="type")
    id: str = Field(None, alias="id")
    timestamp: datetime = Field(None, alias="timestamp")
    local_timestamp: datetime = Field(None, alias="localTimestamp")
    local_timezone: str = Field(None, alias="localTimezone")
    service_url: str = Field(None, alias="serviceUrl")
    channel_id: str = Field(None, alias="channelId")
    from_property: ChannelAccount = Field(None, alias="from")
    conversation: ConversationAccount = Field(None, alias="conversation")
    recipient: ChannelAccount = Field(None, alias="recipient")
    text_format: str = Field(None, alias="textFormat")
    attachment_layout: str = Field(None, alias="attachmentLayout")
    members_added: list[ChannelAccount] = Field(None, alias="membersAdded")
    members_removed: list[ChannelAccount] = Field(None, alias="membersRemoved")
    reactions_added: list[MessageReaction] = Field(None, alias="reactionsAdded")
    reactions_removed: list[MessageReaction] = Field(None, alias="reactionsRemoved")
    topic_name: str = Field(None, alias="topicName")
    history_disclosed: bool = Field(None, alias="historyDisclosed")
    locale: str = Field(None, alias="locale")
    text: str = Field(None, alias="text")
    speak: str = Field(None, alias="speak")
    input_hint: str = Field(None, alias="inputHint")
    summary: str = Field(None, alias="summary")
    suggested_actions: SuggestedActions = Field(None, alias="suggestedActions")
    attachments: list[Attachment] = Field(None, alias="attachments")
    entities: list[Entity] = Field(None, alias="entities")
    channel_data: object = Field(None, alias="channelData")
    action: str = Field(None, alias="action")
    reply_to_id: str = Field(None, alias="replyToId")
    label: str = Field(None, alias="label")
    value_type: str = Field(None, alias="valueType")
    value: object = Field(None, alias="value")
    name: str = Field(None, alias="name")
    relates_to: ConversationReference = Field(None, alias="relatesTo")
    code: str = Field(None, alias="code")
    expiration: datetime = Field(None, alias="expiration")
    importance: str = Field(None, alias="importance")
    delivery_mode: str = Field(None, alias="deliveryMode")
    listen_for: list[str] = Field(None, alias="listenFor")
    text_highlights: list[TextHighlight] = Field(None, alias="textHighlights")
    semantic_action: SemanticAction = Field(None, alias="semanticAction")
    caller_id: str = Field(None, alias="callerId")

    def __init__(
        self,
        *,
        type=None,
        id: str = None,
        timestamp=None,
        local_timestamp=None,
        local_timezone: str = None,
        service_url: str = None,
        channel_id: str = None,
        from_property=None,
        conversation=None,
        recipient=None,
        text_format=None,
        attachment_layout=None,
        members_added=None,
        members_removed=None,
        reactions_added=None,
        reactions_removed=None,
        topic_name: str = None,
        history_disclosed: bool = None,
        locale: str = None,
        text: str = None,
        speak: str = None,
        input_hint=None,
        summary: str = None,
        suggested_actions=None,
        attachments=None,
        entities=None,
        channel_data=None,
        action: str = None,
        reply_to_id: str = None,
        label: str = None,
        value_type: str = None,
        value=None,
        name: str = None,
        relates_to=None,
        code=None,
        expiration=None,
        importance=None,
        delivery_mode=None,
        listen_for=None,
        text_highlights=None,
        semantic_action=None,
        caller_id: str = None,
        **kwargs
    ) -> None:
        super(Activity, self).__init__(**kwargs)
        self.type = type
        self.id = id
        self.timestamp = timestamp
        self.local_timestamp = local_timestamp
        self.local_timezone = local_timezone
        self.service_url = service_url
        self.channel_id = channel_id
        self.from_property = from_property
        self.conversation = conversation
        self.recipient = recipient
        self.text_format = text_format
        self.attachment_layout = attachment_layout
        self.members_added = members_added
        self.members_removed = members_removed
        self.reactions_added = reactions_added
        self.reactions_removed = reactions_removed
        self.topic_name = topic_name
        self.history_disclosed = history_disclosed
        self.locale = locale
        self.text = text
        self.speak = speak
        self.input_hint = input_hint
        self.summary = summary
        self.suggested_actions = suggested_actions
        self.attachments = attachments
        self.entities = entities
        self.channel_data = channel_data
        self.action = action
        self.reply_to_id = reply_to_id
        self.label = label
        self.value_type = value_type
        self.value = value
        self.name = name
        self.relates_to = relates_to
        self.code = code
        self.expiration = expiration
        self.importance = importance
        self.delivery_mode = delivery_mode
        self.listen_for = listen_for
        self.text_highlights = text_highlights
        self.semantic_action = semantic_action
        self.caller_id = caller_id

    def apply_conversation_reference(
        self, reference: ConversationReference, is_incoming: bool = False
    ):
        """
        Updates this activity with the delivery information from an existing ConversationReference

        :param reference: The existing conversation reference.
        :param is_incoming: Optional, True to treat the activity as an
        incoming activity, where the bot is the recipient; otherwise, False.
        Default is False, and the activity will show the bot as the sender.

        :returns: his activity, updated with the delivery information.

        .. remarks::
            Call GetConversationReference on an incoming
            activity to get a conversation reference that you can then use to update an
            outgoing activity with the correct delivery information.
        """
        self.channel_id = reference.channel_id
        self.service_url = reference.service_url
        self.conversation = reference.conversation

        if reference.locale is not None:
            self.locale = reference.locale

        if is_incoming:
            self.from_property = reference.user
            self.recipient = reference.bot

            if reference.activity_id is not None:
                self.id = reference.activity_id
        else:
            self.from_property = reference.bot
            self.recipient = reference.user

            if reference.activity_id is not None:
                self.reply_to_id = reference.activity_id

        return self

    def as_contact_relation_update_activity(self):
        """
        Returns this activity as a ContactRelationUpdateActivity object;
        or None, if this is not that type of activity.

        :returns: This activity as a message activity; or None.
        """
        return (
            self if self.__is_activity(ActivityTypes.contact_relation_update) else None
        )

    def as_conversation_update_activity(self):
        """
        Returns this activity as a ConversationUpdateActivity object;
        or None, if this is not that type of activity.

        :returns: This activity as a conversation update activity; or None.
        """
        return self if self.__is_activity(ActivityTypes.conversation_update) else None

    def as_end_of_conversation_activity(self):
        """
        Returns this activity as an EndOfConversationActivity object;
        or None, if this is not that type of activity.

        :returns: This activity as an end of conversation activity; or None.
        """
        return self if self.__is_activity(ActivityTypes.end_of_conversation) else None

    def as_event_activity(self):
        """
        Returns this activity as an EventActivity object;
        or None, if this is not that type of activity.

        :returns: This activity as an event activity; or None.
        """
        return self if self.__is_activity(ActivityTypes.event) else None

    def as_handoff_activity(self):
        """
        Returns this activity as a HandoffActivity object;
        or None, if this is not that type of activity.

        :returns: This activity as a handoff activity; or None.
        """
        return self if self.__is_activity(ActivityTypes.handoff) else None

    def as_installation_update_activity(self):
        """
        Returns this activity as an InstallationUpdateActivity object;
        or None, if this is not that type of activity.

        :returns: This activity as an installation update activity; or None.
        """
        return self if self.__is_activity(ActivityTypes.installation_update) else None

    def as_invoke_activity(self):
        """
        Returns this activity as an InvokeActivity object;
        or None, if this is not that type of activity.

        :returns: This activity as an invoke activity; or None.
        """
        return self if self.__is_activity(ActivityTypes.invoke) else None

    def as_message_activity(self):
        """
        Returns this activity as a MessageActivity object;
        or None, if this is not that type of activity.

        :returns: This activity as a message activity; or None.
        """
        return self if self.__is_activity(ActivityTypes.message) else None

    def as_message_delete_activity(self):
        """
        Returns this activity as a MessageDeleteActivity object;
        or None, if this is not that type of activity.

        :returns: This activity as a message delete request; or None.
        """
        return self if self.__is_activity(ActivityTypes.message_delete) else None

    def as_message_reaction_activity(self):
        """
        Returns this activity as a MessageReactionActivity object;
        or None, if this is not that type of activity.

        :return: This activity as a message reaction activity; or None.
        """
        return self if self.__is_activity(ActivityTypes.message_reaction) else None

    def as_message_update_activity(self):
        """
        Returns this activity as an MessageUpdateActivity object;
        or None, if this is not that type of activity.

        :returns: This activity as a message update request; or None.
        """
        return self if self.__is_activity(ActivityTypes.message_update) else None

    def as_suggestion_activity(self):
        """
        Returns this activity as a SuggestionActivity object;
        or None, if this is not that type of activity.

        :returns: This activity as a suggestion activity; or None.
        """
        return self if self.__is_activity(ActivityTypes.suggestion) else None

    def as_trace_activity(self):
        """
        Returns this activity as a TraceActivity object;
        or None, if this is not that type of activity.

        :returns: This activity as a trace activity; or None.
        """
        return self if self.__is_activity(ActivityTypes.trace) else None

    def as_typing_activity(self):
        """
        Returns this activity as a TypingActivity object;
        or null, if this is not that type of activity.

        :returns: This activity as a typing activity; or null.
        """
        return self if self.__is_activity(ActivityTypes.typing) else None

    @staticmethod
    def create_contact_relation_update_activity():
        """
        Creates an instance of the :class:`Activity` class as aContactRelationUpdateActivity object.

        :returns: The new contact relation update activity.
        """
        return Activity(type=ActivityTypes.contact_relation_update)

    @staticmethod
    def create_conversation_update_activity():
        """
        Creates an instance of the :class:`Activity` class as a ConversationUpdateActivity object.

        :returns: The new conversation update activity.
        """
        return Activity(type=ActivityTypes.conversation_update)

    @staticmethod
    def create_end_of_conversation_activity():
        """
        Creates an instance of the :class:`Activity` class as an EndOfConversationActivity object.

        :returns: The new end of conversation activity.
        """
        return Activity(type=ActivityTypes.end_of_conversation)

    @staticmethod
    def create_event_activity():
        """
        Creates an instance of the :class:`Activity` class as an EventActivity object.

        :returns: The new event activity.
        """
        return Activity(type=ActivityTypes.event)

    @staticmethod
    def create_handoff_activity():
        """
        Creates an instance of the :class:`Activity` class as a HandoffActivity object.

        :returns: The new handoff activity.
        """
        return Activity(type=ActivityTypes.handoff)

    @staticmethod
    def create_invoke_activity():
        """
        Creates an instance of the :class:`Activity` class as an InvokeActivity object.

        :returns: The new invoke activity.
        """
        return Activity(type=ActivityTypes.invoke)

    @staticmethod
    def create_message_activity():
        """
        Creates an instance of the :class:`Activity` class as a MessageActivity object.

        :returns: The new message activity.
        """
        return Activity(type=ActivityTypes.message)

    def create_reply(self, text: str = None, locale: str = None):
        """
        Creates a new message activity as a response to this activity.

        :param text: The text of the reply.
        :param locale: The language code for the text.

        :returns: The new message activity.

        .. remarks::
            The new activity sets up routing information based on this activity.
        """
        return Activity(
            type=ActivityTypes.message,
            timestamp=datetime.now(timezone.utc),
            from_property=ChannelAccount(
                id=self.recipient.id if self.recipient else None,
                name=self.recipient.name if self.recipient else None,
            ),
            recipient=ChannelAccount(
                id=self.from_property.id if self.from_property else None,
                name=self.from_property.name if self.from_property else None,
            ),
            reply_to_id=(
                self.id
                if type != ActivityTypes.conversation_update
                or self.channel_id not in ["directline", "webchat"]
                else None
            ),
            service_url=self.service_url,
            channel_id=self.channel_id,
            conversation=ConversationAccount(
                is_group=self.conversation.is_group,
                id=self.conversation.id,
                name=self.conversation.name,
            ),
            text=text if text else "",
            locale=locale if locale else self.locale,
            attachments=[],
            entities=[],
        )

    def create_trace(
        self, name: str, value: object = None, value_type: str = None, label: str = None
    ):
        """
        Creates a new trace activity based on this activity.

        :param name: The name of the trace operation to create.
        :param value: Optional, the content for this trace operation.
        :param value_type: Optional, identifier for the format of the value
        Default is the name of type of the value.
        :param label: Optional, a descriptive label for this trace operation.

        :returns: The new trace activity.
        """
        if not value_type and value:
            value_type = type(value)

        return Activity(
            type=ActivityTypes.trace,
            timestamp=datetime.now(timezone.utc),
            from_property=ChannelAccount(
                id=self.recipient.id if self.recipient else None,
                name=self.recipient.name if self.recipient else None,
            ),
            recipient=ChannelAccount(
                id=self.from_property.id if self.from_property else None,
                name=self.from_property.name if self.from_property else None,
            ),
            reply_to_id=(
                self.id
                if type != ActivityTypes.conversation_update
                or self.channel_id not in ["directline", "webchat"]
                else None
            ),
            service_url=self.service_url,
            channel_id=self.channel_id,
            conversation=ConversationAccount(
                is_group=self.conversation.is_group,
                id=self.conversation.id,
                name=self.conversation.name,
            ),
            name=name,
            label=label,
            value_type=value_type,
            value=value,
        ).as_trace_activity()

    @staticmethod
    def create_trace_activity(
        name: str, value: object = None, value_type: str = None, label: str = None
    ):
        """
        Creates an instance of the :class:`Activity` class as a TraceActivity object.

        :param name: The name of the trace operation to create.
        :param value: Optional, the content for this trace operation.
        :param value_type: Optional, identifier for the format of the value.
        Default is the name of type of the value.
        :param label: Optional, a descriptive label for this trace operation.

        :returns: The new trace activity.
        """
        if not value_type and value:
            value_type = type(value)

        return Activity(
            type=ActivityTypes.trace,
            name=name,
            label=label,
            value_type=value_type,
            value=value,
        )

    @staticmethod
    def create_typing_activity():
        """
        Creates an instance of the :class:`Activity` class as a TypingActivity object.

        :returns: The new typing activity.
        """
        return Activity(type=ActivityTypes.typing)

    def get_conversation_reference(self):
        """
        Creates a ConversationReference based on this activity.

        :returns: A conversation reference for the conversation that contains this activity.
        """
        return ConversationReference(
            activity_id=(
                self.id
                if type != ActivityTypes.conversation_update
                or self.channel_id not in ["directline", "webchat"]
                else None
            ),
            user=self.from_property,
            bot=self.recipient,
            conversation=self.conversation,
            channel_id=self.channel_id,
            locale=self.locale,
            service_url=self.service_url,
        )

    def get_mentions(self) -> list[Mention]:
        """
        Resolves the mentions from the entities of this activity.

        :returns: The array of mentions; or an empty array, if none are found.

        .. remarks::
            This method is defined on the :class:`Activity` class, but is only intended
            for use with a message activity, where the activity Activity.Type is set to
            ActivityTypes.Message.
        """
        _list = self.entities
        return [x for x in _list if str(x.type).lower() == "mention"]

    def get_reply_conversation_reference(
        self, reply: ResourceResponse
    ) -> ConversationReference:
        """
        Create a ConversationReference based on this Activity's Conversation info
        and the ResourceResponse from sending an activity.

        :param reply: ResourceResponse returned from send_activity.

        :return: A ConversationReference that can be stored and used later to delete or update the activity.
        """
        reference = self.get_conversation_reference()
        reference.activity_id = reply.id
        return reference

    def has_content(self) -> bool:
        """
        Indicates whether this activity has content.

        :returns: True, if this activity has any content to send; otherwise, false.

        .. remarks::
            This method is defined on the :class:`Activity` class, but is only intended
            for use with a message activity, where the activity Activity.Type is set to
            ActivityTypes.Message.
        """
        if self.text and self.text.strip():
            return True

        if self.summary and self.summary.strip():
            return True

        if self.attachments and len(self.attachments) > 0:
            return True

        if self.channel_data:
            return True

        return False

    def is_from_streaming_connection(self) -> bool:
        """
        Determine if the Activity was sent via an Http/Https connection or Streaming
        This can be determined by looking at the service_url property:
        (1) All channels that send messages via http/https are not streaming
        (2) Channels that send messages via streaming have a ServiceUrl that does not begin with http/https.

        :returns: True if the Activity originated from a streaming connection.
        """
        if self.service_url:
            return not self.service_url.lower().startswith("http")
        return False

    def __is_activity(self, activity_type: str) -> bool:
        """
        Indicates whether this activity is of a specified activity type.

        :param activity_type: The activity type to check for.
        :return: True if this activity is of the specified activity type; otherwise, False.
        """
        if self.type is None:
            return False

        type_attribute = str(self.type).lower()
        activity_type = str(activity_type).lower()

        result = type_attribute.startswith(activity_type)

        if result:
            result = len(type_attribute) == len(activity_type)

            if not result:
                result = (
                    len(type_attribute) > len(activity_type)
                    and type_attribute[len(activity_type)] == "/"
                )

        return result


class AnimationCard(BaseModel):
    """An animation card (Ex: gif or short video clip).

    :param title: Title of this card
    :type title: str
    :param subtitle: Subtitle of this card
    :type subtitle: str
    :param text: Text of this card
    :type text: str
    :param image: Thumbnail placeholder
    :type image: ~microsoft.agents.protocols.models.ThumbnailUrl
    :param media: Media URLs for this card. When this field contains more than
     one URL, each URL is an alternative format of the same content.
    :type media: list[~microsoft.agents.protocols.models.MediaUrl]
    :param buttons: Actions on this card
    :type buttons: list[~microsoft.agents.protocols.models.CardAction]
    :param shareable: This content may be shared with others (default:true)
    :type shareable: bool
    :param autoloop: Should the client loop playback at end of content
     (default:true)
    :type autoloop: bool
    :param autostart: Should the client automatically start playback of media
     in this card (default:true)
    :type autostart: bool
    :param aspect: Aspect ratio of thumbnail/media placeholder. Allowed values
     are "16:9" and "4:3"
    :type aspect: str
    :param duration: Describes the length of the media content without
     requiring a receiver to open the content. Formatted as an ISO 8601
     Duration field.
    :type duration: str
    :param value: Supplementary parameter for this card
    :type value: object
    """

    title: str = Field(None, alias="title")
    subtitle: str = Field(None, alias="subtitle")
    text: str = Field(None, alias="text")
    image: ThumbnailUrl = Field(None, alias="image")
    media: list[MediaUrl] = Field(None, alias="media")
    buttons: list[CardAction] = Field(None, alias="buttons")
    shareable: bool = Field(None, alias="shareable")
    autoloop: bool = Field(None, alias="autoloop")
    autostart: bool = Field(None, alias="autostart")
    aspect: str = Field(None, alias="aspect")
    duration: str = Field(None, alias="duration")
    value: object = Field(None, alias="value")

    def __init__(
        self,
        *,
        title: str = None,
        subtitle: str = None,
        text: str = None,
        image=None,
        media=None,
        buttons=None,
        shareable: bool = None,
        autoloop: bool = None,
        autostart: bool = None,
        aspect: str = None,
        duration: str = None,
        value=None,
        **kwargs
    ) -> None:
        super(AnimationCard, self).__init__(**kwargs)
        self.title = title
        self.subtitle = subtitle
        self.text = text
        self.image = image
        self.media = media
        self.buttons = buttons
        self.shareable = shareable
        self.autoloop = autoloop
        self.autostart = autostart
        self.aspect = aspect
        self.duration = duration
        self.value = value


class Attachment(BaseModel):
    """An attachment within an activity.

    :param content_type: mimetype/Contenttype for the file
    :type content_type: str
    :param content_url: Content Url
    :type content_url: str
    :param content: Embedded content
    :type content: object
    :param name: (OPTIONAL) The name of the attachment
    :type name: str
    :param thumbnail_url: (OPTIONAL) Thumbnail associated with attachment
    :type thumbnail_url: str
    """

    content_type: str = Field(None, alias="contentType")
    content_url: str = Field(None, alias="contentUrl")
    content: object = Field(None, alias="content")
    name: str = Field(None, alias="name")
    thumbnail_url: str = Field(None, alias="thumbnailUrl")

    def __init__(
        self,
        *,
        content_type: str = None,
        content_url: str = None,
        content=None,
        name: str = None,
        thumbnail_url: str = None,
        **kwargs
    ) -> None:
        super(Attachment, self).__init__(**kwargs)
        self.content_type = content_type
        self.content_url = content_url
        self.content = content
        self.name = name
        self.thumbnail_url = thumbnail_url


class AttachmentData(BaseModel):
    """Attachment data.

    :param type: Content-Type of the attachment
    :type type: str
    :param name: Name of the attachment
    :type name: str
    :param original_base64: Attachment content
    :type original_base64: bytearray
    :param thumbnail_base64: Attachment thumbnail
    :type thumbnail_base64: bytearray
    """

    type: str = Field(None, alias="type")
    name: str = Field(None, alias="name")
    original_base64: bytearray = Field(None, alias="originalBase64")
    thumbnail_base64: bytearray = Field(None, alias="thumbnailBase64")

    def __init__(
        self,
        *,
        type: str = None,
        name: str = None,
        original_base64: bytearray = None,
        thumbnail_base64: bytearray = None,
        **kwargs
    ) -> None:
        super(AttachmentData, self).__init__(**kwargs)
        self.type = type
        self.name = name
        self.original_base64 = original_base64
        self.thumbnail_base64 = thumbnail_base64


class AttachmentInfo(BaseModel):
    """Metadata for an attachment.

    :param name: Name of the attachment
    :type name: str
    :param type: ContentType of the attachment
    :type type: str
    :param views: attachment views
    :type views: list[~microsoft.agents.protocols.models.AttachmentView]
    """

    name: str = Field(None, alias="name")
    type: str = Field(None, alias="type")
    views: list[AttachmentView] = Field(None, alias="views")

    def __init__(
        self, *, name: str = None, type: str = None, views=None, **kwargs
    ) -> None:
        super(AttachmentInfo, self).__init__(**kwargs)
        self.name = name
        self.type = type
        self.views = views


class AttachmentView(BaseModel):
    """Attachment View name and size.

    :param view_id: Id of the attachment
    :type view_id: str
    :param size: Size of the attachment
    :type size: int
    """

    view_id: str = Field(None, alias="viewId")
    size: int = Field(None, alias="size")

    def __init__(self, *, view_id: str = None, size: int = None, **kwargs) -> None:
        super(AttachmentView, self).__init__(**kwargs)
        self.view_id = view_id
        self.size = size


class AudioCard(BaseModel):
    """Audio card.

    :param title: Title of this card
    :type title: str
    :param subtitle: Subtitle of this card
    :type subtitle: str
    :param text: Text of this card
    :type text: str
    :param image: Thumbnail placeholder
    :type image: ~microsoft.agents.protocols.models.ThumbnailUrl
    :param media: Media URLs for this card. When this field contains more than
     one URL, each URL is an alternative format of the same content.
    :type media: list[~microsoft.agents.protocols.models.MediaUrl]
    :param buttons: Actions on this card
    :type buttons: list[~microsoft.agents.protocols.models.CardAction]
    :param shareable: This content may be shared with others (default:true)
    :type shareable: bool
    :param autoloop: Should the client loop playback at end of content
     (default:true)
    :type autoloop: bool
    :param autostart: Should the client automatically start playback of media
     in this card (default:true)
    :type autostart: bool
    :param aspect: Aspect ratio of thumbnail/media placeholder. Allowed values
     are "16:9" and "4:3"
    :type aspect: str
    :param duration: Describes the length of the media content without
     requiring a receiver to open the content. Formatted as an ISO 8601
     Duration field.
    :type duration: str
    :param value: Supplementary parameter for this card
    :type value: object
    """

    title: str = Field(None, alias="title")
    subtitle: str = Field(None, alias="subtitle")
    text: str = Field(None, alias="text")
    image: ThumbnailUrl = Field(None, alias="image")
    media: list[MediaUrl] = Field(None, alias="media")
    buttons: list[CardAction] = Field(None, alias="buttons")
    shareable: bool = Field(None, alias="shareable")
    autoloop: bool = Field(None, alias="autoloop")
    autostart: bool = Field(None, alias="autostart")
    aspect: str = Field(None, alias="aspect")
    duration: str = Field(None, alias="duration")
    value: object = Field(None, alias="value")

    def __init__(
        self,
        *,
        title: str = None,
        subtitle: str = None,
        text: str = None,
        image=None,
        media=None,
        buttons=None,
        shareable: bool = None,
        autoloop: bool = None,
        autostart: bool = None,
        aspect: str = None,
        duration: str = None,
        value=None,
        **kwargs
    ) -> None:
        super(AudioCard, self).__init__(**kwargs)
        self.title = title
        self.subtitle = subtitle
        self.text = text
        self.image = image
        self.media = media
        self.buttons = buttons
        self.shareable = shareable
        self.autoloop = autoloop
        self.autostart = autostart
        self.aspect = aspect
        self.duration = duration
        self.value = value


class BasicCard(BaseModel):
    """A basic card.

    :param title: Title of the card
    :type title: str
    :param subtitle: Subtitle of the card
    :type subtitle: str
    :param text: Text for the card
    :type text: str
    :param images: Array of images for the card
    :type images: list[~microsoft.agents.protocols.models.CardImage]
    :param buttons: Set of actions applicable to the current card
    :type buttons: list[~microsoft.agents.protocols.models.CardAction]
    :param tap: This action will be activated when user taps on the card
     itself
    :type tap: ~microsoft.agents.protocols.models.CardAction
    """

    title: str = Field(None, alias="title")
    subtitle: str = Field(None, alias="subtitle")
    text: str = Field(None, alias="text")
    images: list[CardImage] = Field(None, alias="images")
    buttons: list[CardAction] = Field(None, alias="buttons")
    tap: CardAction = Field(None, alias="tap")

    def __init__(
        self,
        *,
        title: str = None,
        subtitle: str = None,
        text: str = None,
        images=None,
        buttons=None,
        tap=None,
        **kwargs
    ) -> None:
        super(BasicCard, self).__init__(**kwargs)
        self.title = title
        self.subtitle = subtitle
        self.text = text
        self.images = images
        self.buttons = buttons
        self.tap = tap


class CardAction(BaseModel):
    """A clickable action.

    :param type: The type of action implemented by this button. Possible
     values include: 'openUrl', 'imBack', 'postBack', 'playAudio', 'playVideo',
     'showImage', 'downloadFile', 'signin', 'call', 'messageBack'
    :type type: str or ~microsoft.agents.protocols.models.ActionTypes
    :param title: Text description which appears on the button
    :type title: str
    :param image: Image URL which will appear on the button, next to text
     label
    :type image: str
    :param text: Text for this action
    :type text: str
    :param display_text: (Optional) text to display in the chat feed if the
     button is clicked
    :type display_text: str
    :param value: Supplementary parameter for action. Content of this property
     depends on the ActionType
    :type value: object
    :param channel_data: Channel-specific data associated with this action
    :type channel_data: object
    :param image_alt_text: Alternate image text to be used in place of the `image` field
    :type image_alt_text: str
    """

    type: str = Field(None, alias="type")
    title: str = Field(None, alias="title")
    image: str = Field(None, alias="image")
    text: str = Field(None, alias="text")
    display_text: str = Field(None, alias="displayText")
    value: object = Field(None, alias="value")
    channel_data: object = Field(None, alias="channelData")
    image_alt_text: str = Field(None, alias="imageAltText")

    def __init__(
        self,
        *,
        type=None,
        title: str = None,
        image: str = None,
        text: str = None,
        display_text: str = None,
        value=None,
        channel_data=None,
        image_alt_text: str = None,
        **kwargs
    ) -> None:
        super(CardAction, self).__init__(**kwargs)
        self.type = type
        self.title = title
        self.image = image
        self.text = text
        self.display_text = display_text
        self.value = value
        self.channel_data = channel_data
        self.image_alt_text = image_alt_text


class CardImage(BaseModel):
    """An image on a card.

    :param url: URL thumbnail image for major content property
    :type url: str
    :param alt: Image description intended for screen readers
    :type alt: str
    :param tap: Action assigned to specific Attachment
    :type tap: ~microsoft.agents.protocols.models.CardAction
    """

    url: str = Field(None, alias="url")
    alt: str = Field(None, alias="alt")
    tap: CardAction = Field(None, alias="tap")

    def __init__(self, *, url: str = None, alt: str = None, tap=None, **kwargs) -> None:
        super(CardImage, self).__init__(**kwargs)
        self.url = url
        self.alt = alt
        self.tap = tap


class ChannelAccount(BaseModel):
    """Channel account information needed to route a message.

    :param id: Channel id for the user or bot on this channel (Example:
     joe@smith.com, or @joesmith or 123456)
    :type id: str
    :param name: Display friendly name
    :type name: str
    :param aad_object_id: This account's object ID within Azure Active
     Directory (AAD)
    :type aad_object_id: str
    :param role: Role of the entity behind the account (Example: User, Bot,
     etc.). Possible values include: 'user', 'bot'
    :type role: str or ~microsoft.agents.protocols.models.RoleTypes
    """

    id: str = Field(None, alias="id")
    name: str = Field(None, alias="name")
    aad_object_id: str = Field(None, alias="aadObjectId")
    role: str = Field(None, alias="role")
    properties: object = Field(None, alias="properties")

    def __init__(
        self,
        *,
        id: str = None,
        name: str = None,
        aad_object_id: str = None,
        role=None,
        properties=None,
        **kwargs
    ) -> None:
        super(ChannelAccount, self).__init__(**kwargs)
        self.id = id
        self.name = name
        self.aad_object_id = aad_object_id
        self.role = role
        self.properties = properties


class ConversationAccount(BaseModel):
    """Conversation account represents the identity of the conversation within a channel.

    :param is_group: Indicates whether the conversation contains more than two
     participants at the time the activity was generated
    :type is_group: bool
    :param conversation_type: Indicates the type of the conversation in
     channels that distinguish between conversation types
    :type conversation_type: str
    :param id: Channel id for the user or bot on this channel (Example:
     joe@smith.com, or @joesmith or 123456)
    :type id: str
    :param name: Display friendly name
    :type name: str
    :param aad_object_id: This account's object ID within Azure Active
     Directory (AAD)
    :type aad_object_id: str
    :param role: Role of the entity behind the account (Example: User, Bot, Skill
     etc.). Possible values include: 'user', 'bot', 'skill'
    :type role: str or ~microsoft.agents.protocols.models.RoleTypes
    :param tenant_id: This conversation's tenant ID
    :type tenant_id: str
    :param properties: This conversation's properties
    :type properties: object
    """

    is_group: bool = Field(None, alias="isGroup")
    conversation_type: str = Field(None, alias="conversationType")
    id: str = Field(None, alias="id")
    name: str = Field(None, alias="name")
    aad_object_id: str = Field(None, alias="aadObjectId")
    role: str = Field(None, alias="role")
    tenant_id: str = Field(None, alias="tenantID")
    properties: object = Field(None, alias="properties")

    def __init__(
        self,
        *,
        is_group: bool = None,
        conversation_type: str = None,
        id: str = None,
        name: str = None,
        aad_object_id: str = None,
        role=None,
        tenant_id=None,
        properties=None,
        **kwargs
    ) -> None:
        super(ConversationAccount, self).__init__(**kwargs)
        self.is_group = is_group
        self.conversation_type = conversation_type
        self.id = id
        self.name = name
        self.aad_object_id = aad_object_id
        self.role = role
        self.tenant_id = tenant_id
        self.properties = properties


class ConversationMembers(BaseModel):
    """Conversation and its members.

    :param id: Conversation ID
    :type id: str
    :param members: List of members in this conversation
    :type members: list[~microsoft.agents.protocols.models.ChannelAccount]
    """

    id: str = Field(None, alias="id")
    members: list[ChannelAccount] = Field(None, alias="members")

    def __init__(self, *, id: str = None, members=None, **kwargs) -> None:
        super(ConversationMembers, self).__init__(**kwargs)
        self.id = id
        self.members = members


class ConversationParameters(BaseModel):
    """Parameters for creating a new conversation.

    :param is_group: IsGroup
    :type is_group: bool
    :param bot: The bot address for this conversation
    :type bot: ~microsoft.agents.protocols.models.ChannelAccount
    :param members: Members to add to the conversation
    :type members: list[~microsoft.agents.protocols.models.ChannelAccount]
    :param topic_name: (Optional) Topic of the conversation (if supported by
     the channel)
    :type topic_name: str
    :param activity: (Optional) When creating a new conversation, use this
     activity as the initial message to the conversation
    :type activity: ~microsoft.agents.protocols.models.Activity
    :param channel_data: Channel specific payload for creating the
     conversation
    :type channel_data: object
    :param tenant_id: (Optional) The tenant ID in which the conversation should be created
    :type tenant_id: str
    """

    is_group: bool = Field(None, alias="isGroup")
    bot: ChannelAccount = Field(None, alias="bot")
    members: list[ChannelAccount] = Field(None, alias="members")
    topic_name: str = Field(None, alias="topicName")
    activity: Activity = Field(None, alias="activity")
    channel_data: object = Field(None, alias="channelData")
    tenant_id: str = Field(None, alias="tenantID")

    def __init__(
        self,
        *,
        is_group: bool = None,
        bot=None,
        members=None,
        topic_name: str = None,
        activity=None,
        channel_data=None,
        tenant_id=None,
        **kwargs
    ) -> None:
        super(ConversationParameters, self).__init__(**kwargs)
        self.is_group = is_group
        self.bot = bot
        self.members = members
        self.topic_name = topic_name
        self.activity = activity
        self.channel_data = channel_data
        self.tenant_id = tenant_id


class ConversationResourceResponse(BaseModel):
    """A response containing a resource.

    :param activity_id: ID of the Activity (if sent)
    :type activity_id: str
    :param service_url: Service endpoint where operations concerning the
     conversation may be performed
    :type service_url: str
    :param id: Id of the resource
    :type id: str
    """

    activity_id: str = Field(None, alias="activityId")
    service_url: str = Field(None, alias="serviceUrl")
    id: str = Field(None, alias="id")

    def __init__(
        self,
        *,
        activity_id: str = None,
        service_url: str = None,
        id: str = None,
        **kwargs
    ) -> None:
        super(ConversationResourceResponse, self).__init__(**kwargs)
        self.activity_id = activity_id
        self.service_url = service_url
        self.id = id


class ConversationsResult(BaseModel):
    """Conversations result.

    :param continuation_token: Paging token
    :type continuation_token: str
    :param conversations: List of conversations
    :type conversations:
     list[~microsoft.agents.protocols.models.ConversationMembers]
    """

    continuation_token: str = Field(None, alias="continuationToken")
    conversations: list[ConversationMembers] = Field(None, alias="conversations")

    def __init__(
        self, *, continuation_token: str = None, conversations=None, **kwargs
    ) -> None:
        super(ConversationsResult, self).__init__(**kwargs)
        self.continuation_token = continuation_token
        self.conversations = conversations


class ExpectedReplies(BaseModel):
    """ExpectedReplies.

    :param activities: A collection of Activities that conforms to the
     ExpectedReplies schema.
    :type activities: list[~microsoft.agents.protocols.models.Activity]
    """

    activities: list[Activity] = Field(None, alias="activities")

    def __init__(self, *, activities=None, **kwargs) -> None:
        super(ExpectedReplies, self).__init__(**kwargs)
        self.activities = activities


class Entity(BaseModel):
    """Metadata object pertaining to an activity.

    :param type: Type of this entity (RFC 3987 IRI)
    :type type: str
    """

    type: str = Field(None, alias="type")

    def __init__(self, *, type: str = None, **kwargs) -> None:
        super(Entity, self).__init__(**kwargs)
        self.type = type


class Error(BaseModel):
    """Object representing error information.

    :param code: Error code
    :type code: str
    :param message: Error message
    :type message: str
    :param inner_http_error: Error from inner http call
    :type inner_http_error: ~microsoft.agents.protocols.models.InnerHttpError
    """

    code: str = Field(None, alias="code")
    message: str = Field(None, alias="message")
    inner_http_error: InnerHttpError = Field(None, alias="innerHttpError")

    def __init__(
        self, *, code: str = None, message: str = None, inner_http_error=None, **kwargs
    ) -> None:
        super(Error, self).__init__(**kwargs)
        self.code = code
        self.message = message
        self.inner_http_error = inner_http_error


class ErrorResponse(BaseModel):
    """An HTTP API response.

    :param error: Error message
    :type error: ~microsoft.agents.protocols.models.Error
    """

    error: Error = Field(None, alias="error")

    def __init__(self, *, error=None, **kwargs) -> None:
        super(ErrorResponse, self).__init__(**kwargs)
        self.error = error


class ErrorResponseException(HttpOperationError):
    """Server responsed with exception of type: 'ErrorResponse'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):
        super(ErrorResponseException, self).__init__(
            deserialize, response, "ErrorResponse", *args
        )


class Fact(BaseModel):
    """Set of key-value pairs. Advantage of this section is that key and value
    properties will be
    rendered with default style information with some delimiter between them.
    So there is no need for developer to specify style information.

    :param key: The key for this Fact
    :type key: str
    :param value: The value for this Fact
    :type value: str
    """

    key: str = Field(None, alias="key")
    value: str = Field(None, alias="value")

    def __init__(self, *, key: str = None, value: str = None, **kwargs) -> None:
        super(Fact, self).__init__(**kwargs)
        self.key = key
        self.value = value


class GeoCoordinates(BaseModel):
    """GeoCoordinates (entity type: "https://schema.org/GeoCoordinates").

    :param elevation: Elevation of the location [WGS
     84](https://en.wikipedia.org/wiki/World_Geodetic_System)
    :type elevation: float
    :param latitude: Latitude of the location [WGS
     84](https://en.wikipedia.org/wiki/World_Geodetic_System)
    :type latitude: float
    :param longitude: Longitude of the location [WGS
     84](https://en.wikipedia.org/wiki/World_Geodetic_System)
    :type longitude: float
    :param type: The type of the thing
    :type type: str
    :param name: The name of the thing
    :type name: str
    """

    elevation: float = Field(None, alias="elevation")
    latitude: float = Field(None, alias="latitude")
    longitude: float = Field(None, alias="longitude")
    type: str = Field(None, alias="type")
    name: str = Field(None, alias="name")

    def __init__(
        self,
        *,
        elevation: float = None,
        latitude: float = None,
        longitude: float = None,
        type: str = None,
        name: str = None,
        **kwargs
    ) -> None:
        super(GeoCoordinates, self).__init__(**kwargs)
        self.elevation = elevation
        self.latitude = latitude
        self.longitude = longitude
        self.type = type
        self.name = name


class HeroCard(BaseModel):
    """A Hero card (card with a single, large image).

    :param title: Title of the card
    :type title: str
    :param subtitle: Subtitle of the card
    :type subtitle: str
    :param text: Text for the card
    :type text: str
    :param images: Array of images for the card
    :type images: list[~microsoft.agents.protocols.models.CardImage]
    :param buttons: Set of actions applicable to the current card
    :type buttons: list[~microsoft.agents.protocols.models.CardAction]
    :param tap: This action will be activated when user taps on the card
     itself
    :type tap: ~microsoft.agents.protocols.models.CardAction
    """

    title: str = Field(None, alias="title")
    subtitle: str = Field(None, alias="subtitle")
    text: str = Field(None, alias="text")
    images: list[CardImage] = Field(None, alias="images")
    buttons: list[CardAction] = Field(None, alias="buttons")
    tap: CardAction = Field(None, alias="tap")

    def __init__(
        self,
        *,
        title: str = None,
        subtitle: str = None,
        text: str = None,
        images=None,
        buttons=None,
        tap=None,
        **kwargs
    ) -> None:
        super(HeroCard, self).__init__(**kwargs)
        self.title = title
        self.subtitle = subtitle
        self.text = text
        self.images = images
        self.buttons = buttons
        self.tap = tap


class InnerHttpError(BaseModel):
    """Object representing inner http error.

    :param status_code: HttpStatusCode from failed request
    :type status_code: int
    :param body: Body from failed request
    :type body: object
    """

    status_code: int = Field(None, alias="statusCode")
    body: object = Field(None, alias="body")

    def __init__(self, *, status_code: int = None, body=None, **kwargs) -> None:
        super(InnerHttpError, self).__init__(**kwargs)
        self.status_code = status_code
        self.body = body


class InvokeResponse(BaseModel):
    """
    Tuple class containing an HTTP Status Code and a JSON serializable
    object. The HTTP Status code is, in the invoke activity scenario, what will
    be set in the resulting POST. The Body of the resulting POST will be
    JSON serialized content.

    The body content is defined by the producer.  The caller must know what
    the content is and deserialize as needed.
    """

    status: int = Field(None, alias="status")
    body: object = Field(None, alias="body")

    def __init__(self, *, status: int = None, body: object = None, **kwargs):
        """
        Gets or sets the HTTP status and/or body code for the response
        :param status: The HTTP status code.
        :param body: The JSON serializable body content for the response.  This object
        must be serializable by the core Python json routines.  The caller is responsible
        for serializing more complex/nested objects into native classes (lists and
        dictionaries of strings are acceptable).
        """
        super().__init__(**kwargs)
        self.status = status
        self.body = body

    def is_successful_status_code(self) -> bool:
        """
        Gets a value indicating whether the invoke response was successful.
        :return: A value that indicates if the HTTP response was successful. true if status is in
        the Successful range (200-299); otherwise false.
        """
        return 200 <= self.status <= 299


class MediaCard(BaseModel):
    """Media card.

    :param title: Title of this card
    :type title: str
    :param subtitle: Subtitle of this card
    :type subtitle: str
    :param text: Text of this card
    :type text: str
    :param image: Thumbnail placeholder
    :type image: ~microsoft.agents.protocols.models.ThumbnailUrl
    :param media: Media URLs for this card. When this field contains more than
     one URL, each URL is an alternative format of the same content.
    :type media: list[~microsoft.agents.protocols.models.MediaUrl]
    :param buttons: Actions on this card
    :type buttons: list[~microsoft.agents.protocols.models.CardAction]
    :param shareable: This content may be shared with others (default:true)
    :type shareable: bool
    :param autoloop: Should the client loop playback at end of content
     (default:true)
    :type autoloop: bool
    :param autostart: Should the client automatically start playback of media
     in this card (default:true)
    :type autostart: bool
    :param aspect: Aspect ratio of thumbnail/media placeholder. Allowed values
     are "16:9" and "4:3"
    :type aspect: str
    :param duration: Describes the length of the media content without
     requiring a receiver to open the content. Formatted as an ISO 8601
     Duration field.
    :type duration: str
    :param value: Supplementary parameter for this card
    :type value: object
    """

    title: str = Field(None, alias="title")
    subtitle: str = Field(None, alias="subtitle")
    text: str = Field(None, alias="text")
    image: ThumbnailUrl = Field(None, alias="image")
    media: list[MediaUrl] = Field(None, alias="media")
    buttons: list[CardAction] = Field(None, alias="buttons")
    shareable: bool = Field(None, alias="shareable")
    autoloop: bool = Field(None, alias="autoloop")
    autostart: bool = Field(None, alias="autostart")
    aspect: str = Field(None, alias="aspect")
    duration: str = Field(None, alias="duration")
    value: object = Field(None, alias="value")

    def __init__(
        self,
        *,
        title: str = None,
        subtitle: str = None,
        text: str = None,
        image=None,
        media=None,
        buttons=None,
        shareable: bool = None,
        autoloop: bool = None,
        autostart: bool = None,
        aspect: str = None,
        duration: str = None,
        value=None,
        **kwargs
    ) -> None:
        super(MediaCard, self).__init__(**kwargs)
        self.title = title
        self.subtitle = subtitle
        self.text = text
        self.image = image
        self.media = media
        self.buttons = buttons
        self.shareable = shareable
        self.autoloop = autoloop
        self.autostart = autostart
        self.aspect = aspect
        self.duration = duration
        self.value = value


class MediaEventValue(BaseModel):
    """Supplementary parameter for media events.

    :param card_value: Callback parameter specified in the Value field of the
     MediaCard that originated this event
    :type card_value: object
    """

    card_value: object = Field(None, alias="cardValue")

    def __init__(self, *, card_value=None, **kwargs) -> None:
        super(MediaEventValue, self).__init__(**kwargs)
        self.card_value = card_value


class MediaUrl(BaseModel):
    """Media URL.

    :param url: Url for the media
    :type url: str
    :param profile: Optional profile hint to the client to differentiate
     multiple MediaUrl objects from each other
    :type profile: str
    """

    url: str = Field(None, alias="url")
    profile: str = Field(None, alias="profile")

    def __init__(self, *, url: str = None, profile: str = None, **kwargs) -> None:
        super(MediaUrl, self).__init__(**kwargs)
        self.url = url
        self.profile = profile


class MessageReaction(BaseModel):
    """Message reaction object.

    :param type: Message reaction type. Possible values include: 'like',
     'plusOne'
    :type type: str or ~microsoft.agents.protocols.models.MessageReactionTypes
    """

    type: str = Field(None, alias="type")

    def __init__(self, *, type=None, **kwargs) -> None:
        super(MessageReaction, self).__init__(**kwargs)
        self.type = type


class OAuthCard(BaseModel):
    """A card representing a request to perform a sign in via OAuth.

    :param text: Text for signin request
    :type text: str
    :param connection_name: The name of the registered connection
    :type connection_name: str
    :param buttons: Action to use to perform signin
    :type buttons: list[~microsoft.agents.protocols.models.CardAction]
    """

    text: str = Field(None, alias="text")
    connection_name: str = Field(None, alias="connectionName")
    buttons: list[CardAction] = Field(None, alias="buttons")
    token_exchange_resource: object = Field(None, alias="tokenExchangeResource")

    def __init__(
        self,
        *,
        text: str = None,
        connection_name: str = None,
        buttons=None,
        token_exchange_resource=None,
        **kwargs
    ) -> None:
        super(OAuthCard, self).__init__(**kwargs)
        self.text = text
        self.connection_name = connection_name
        self.buttons = buttons
        self.token_exchange_resource = token_exchange_resource


class PagedMembersResult(BaseModel):
    """Page of members.

    :param continuation_token: Paging token
    :type continuation_token: str
    :param members: The Channel Accounts.
    :type members: list[~microsoft.agents.protocols.models.ChannelAccount]
    """

    continuation_token: str = Field(None, alias="continuationToken")
    members: list[ChannelAccount] = Field(None, alias="members")

    def __init__(
        self, *, continuation_token: str = None, members=None, **kwargs
    ) -> None:
        super(PagedMembersResult, self).__init__(**kwargs)
        self.continuation_token = continuation_token
        self.members = members


class Place(BaseModel):
    """Place (entity type: "https://schema.org/Place").

    :param address: Address of the place (may be `string` or complex object of
     type `PostalAddress`)
    :type address: object
    :param geo: Geo coordinates of the place (may be complex object of type
     `GeoCoordinates` or `GeoShape`)
    :type geo: object
    :param has_map: Map to the place (may be `string` (URL) or complex object
     of type `Map`)
    :type has_map: object
    :param type: The type of the thing
    :type type: str
    :param name: The name of the thing
    :type name: str
    """

    address: object = Field(None, alias="address")
    geo: object = Field(None, alias="geo")
    has_map: object = Field(None, alias="hasMap")
    type: str = Field(None, alias="type")
    name: str = Field(None, alias="name")

    def __init__(
        self,
        *,
        address=None,
        geo=None,
        has_map=None,
        type: str = None,
        name: str = None,
        **kwargs
    ) -> None:
        super(Place, self).__init__(**kwargs)
        self.address = address
        self.geo = geo
        self.has_map = has_map
        self.type = type
        self.name = name


class ReceiptCard(BaseModel):
    """A receipt card.

    :param title: Title of the card
    :type title: str
    :param facts: Array of Fact objects
    :type facts: list[~microsoft.agents.protocols.models.Fact]
    :param items: Array of Receipt Items
    :type items: list[~microsoft.agents.protocols.models.ReceiptItem]
    :param tap: This action will be activated when user taps on the card
    :type tap: ~microsoft.agents.protocols.models.CardAction
    :param total: Total amount of money paid (or to be paid)
    :type total: str
    :param tax: Total amount of tax paid (or to be paid)
    :type tax: str
    :param vat: Total amount of VAT paid (or to be paid)
    :type vat: str
    :param buttons: Set of actions applicable to the current card
    :type buttons: list[~microsoft.agents.protocols.models.CardAction]
    """

    title: str = Field(None, alias="title")
    facts: list[Fact] = Field(None, alias="facts")
    items: list[ReceiptItem] = Field(None, alias="items")
    tap: CardAction = Field(None, alias="tap")
    total: str = Field(None, alias="total")
    tax: str = Field(None, alias="tax")
    vat: str = Field(None, alias="vat")
    buttons: list[CardAction] = Field(None, alias="buttons")

    def __init__(
        self,
        *,
        title: str = None,
        facts=None,
        items=None,
        tap=None,
        total: str = None,
        tax: str = None,
        vat: str = None,
        buttons=None,
        **kwargs
    ) -> None:
        super(ReceiptCard, self).__init__(**kwargs)
        self.title = title
        self.facts = facts
        self.items = items
        self.tap = tap
        self.total = total
        self.tax = tax
        self.vat = vat
        self.buttons = buttons


class ReceiptItem(BaseModel):
    """An item on a receipt card.

    :param title: Title of the Card
    :type title: str
    :param subtitle: Subtitle appears just below Title field, differs from
     Title in font styling only
    :type subtitle: str
    :param text: Text field appears just below subtitle, differs from Subtitle
     in font styling only
    :type text: str
    :param image: Image
    :type image: ~microsoft.agents.protocols.models.CardImage
    :param price: Amount with currency
    :type price: str
    :param quantity: Number of items of given kind
    :type quantity: str
    :param tap: This action will be activated when user taps on the Item
     bubble.
    :type tap: ~microsoft.agents.protocols.models.CardAction
    """

    title: str = Field(None, alias="title")
    subtitle: str = Field(None, alias="subtitle")
    text: str = Field(None, alias="text")
    image: CardImage = Field(None, alias="image")
    price: str = Field(None, alias="price")
    quantity: str = Field(None, alias="quantity")
    tap: CardAction = Field(None, alias="tap")

    def __init__(
        self,
        *,
        title: str = None,
        subtitle: str = None,
        text: str = None,
        image=None,
        price: str = None,
        quantity: str = None,
        tap=None,
        **kwargs
    ) -> None:
        super(ReceiptItem, self).__init__(**kwargs)
        self.title = title
        self.subtitle = subtitle
        self.text = text
        self.image = image
        self.price = price
        self.quantity = quantity
        self.tap = tap


class SemanticAction(BaseModel):
    """Represents a reference to a programmatic action.

    :param id: ID of this action
    :type id: str
    :param entities: Entities associated with this action
    :type entities: dict[str, ~microsoft.agents.protocols.models.Entity]
    :param state: State of this action. Allowed values: `start`, `continue`, `done`
    :type state: str or ~microsoft.agents.protocols.models.SemanticActionStates
    """

    id: str = Field(None, alias="id")
    entities: dict = Field(None, alias="entities")
    state: str = Field(None, alias="state")

    def __init__(self, *, id: str = None, entities=None, state=None, **kwargs) -> None:
        super(SemanticAction, self).__init__(**kwargs)
        self.id = id
        self.entities = entities
        self.state = state


class SigninCard(BaseModel):
    """A card representing a request to sign in.

    :param text: Text for signin request
    :type text: str
    :param buttons: Action to use to perform signin
    :type buttons: list[~microsoft.agents.protocols.models.CardAction]
    """

    text: str = Field(None, alias="text")
    buttons: list[CardAction] = Field(None, alias="buttons")

    def __init__(self, *, text: str = None, buttons=None, **kwargs) -> None:
        super(SigninCard, self).__init__(**kwargs)
        self.text = text
        self.buttons = buttons


class SuggestedActions(BaseModel):
    """SuggestedActions that can be performed.

    :param to: Ids of the recipients that the actions should be shown to.
     These Ids are relative to the channelId and a subset of all recipients of
     the activity
    :type to: list[str]
    :param actions: Actions that can be shown to the user
    :type actions: list[~microsoft.agents.protocols.models.CardAction]
    """

    to: list[str] = Field(None, alias="to")
    actions: list[CardAction] = Field(None, alias="actions")

    def __init__(self, *, to=None, actions=None, **kwargs) -> None:
        super(SuggestedActions, self).__init__(**kwargs)
        self.to = to
        self.actions = actions


class TextHighlight(BaseModel):
    """Refers to a substring of content within another field.

    :param text: Defines the snippet of text to highlight
    :type text: str
    :param occurrence: Occurrence of the text field within the referenced
     text, if multiple exist.
    :type occurrence: int
    """

    text: str = Field(None, alias="text")
    occurrence: int = Field(None, alias="occurrence")

    def __init__(self, *, text: str = None, occurrence: int = None, **kwargs) -> None:
        super(TextHighlight, self).__init__(**kwargs)
        self.text = text
        self.occurrence = occurrence


class Thing(BaseModel):
    """Thing (entity type: "https://schema.org/Thing").

    :param type: The type of the thing
    :type type: str
    :param name: The name of the thing
    :type name: str
    """

    type: str = Field(None, alias="type")
    name: str = Field(None, alias="name")

    def __init__(self, *, type: str = None, name: str = None, **kwargs) -> None:
        super(Thing, self).__init__(**kwargs)
        self.type = type
        self.name = name


class ThumbnailCard(BaseModel):
    """A thumbnail card (card with a single, small thumbnail image).

    :param title: Title of the card
    :type title: str
    :param subtitle: Subtitle of the card
    :type subtitle: str
    :param text: Text for the card
    :type text: str
    :param images: Array of images for the card
    :type images: list[~microsoft.agents.protocols.models.CardImage]
    :param buttons: Set of actions applicable to the current card
    :type buttons: list[~microsoft.agents.protocols.models.CardAction]
    :param tap: This action will be activated when user taps on the card
     itself
    :type tap: ~microsoft.agents.protocols.models.CardAction
    """

    title: str = Field(None, alias="title")
    subtitle: str = Field(None, alias="subtitle")
    text: str = Field(None, alias="text")
    images: list[CardImage] = Field(None, alias="images")
    buttons: list[CardAction] = Field(None, alias="buttons")
    tap: CardAction = Field(None, alias="tap")

    def __init__(
        self,
        *,
        title: str = None,
        subtitle: str = None,
        text: str = None,
        images=None,
        buttons=None,
        tap=None,
        **kwargs
    ) -> None:
        super(ThumbnailCard, self).__init__(**kwargs)
        self.title = title
        self.subtitle = subtitle
        self.text = text
        self.images = images
        self.buttons = buttons
        self.tap = tap


class ThumbnailUrl(BaseModel):
    """Thumbnail URL.

    :param url: URL pointing to the thumbnail to use for media content
    :type url: str
    :param alt: HTML alt text to include on this thumbnail image
    :type alt: str
    """

    url: str = Field(None, alias="url")
    alt: str = Field(None, alias="alt")

    def __init__(self, *, url: str = None, alt: str = None, **kwargs) -> None:
        super(ThumbnailUrl, self).__init__(**kwargs)
        self.url = url
        self.alt = alt


class TokenExchangeInvokeRequest(BaseModel):
    """TokenExchangeInvokeRequest.

    :param id: The id from the OAuthCard.
    :type id: str
    :param connection_name: The connection name.
    :type connection_name: str
    :param token: The user token that can be exchanged.
    :type token: str
    :param properties: Extension data for overflow of properties.
    :type properties: dict[str, object]
    """

    id: str = Field(None, alias="id")
    connection_name: str = Field(None, alias="connectionName")
    token: str = Field(None, alias="token")
    properties: dict = Field(None, alias="properties")

    def __init__(
        self,
        *,
        id: str = None,
        connection_name: str = None,
        token: str = None,
        properties=None,
        **kwargs
    ) -> None:
        super(TokenExchangeInvokeRequest, self).__init__(**kwargs)
        self.id = id
        self.connection_name = connection_name
        self.token = token
        self.properties = properties


class TokenExchangeInvokeResponse(BaseModel):
    """TokenExchangeInvokeResponse.

    :param id: The id from the OAuthCard.
    :type id: str
    :param connection_name: The connection name.
    :type connection_name: str
    :param failure_detail: The details of why the token exchange failed.
    :type failure_detail: str
    :param properties: Extension data for overflow of properties.
    :type properties: dict[str, object]
    """

    id: str = Field(None, alias="id")
    connection_name: str = Field(None, alias="connectionName")
    failure_detail: str = Field(None, alias="failureDetail")
    properties: dict = Field(None, alias="properties")

    def __init__(
        self,
        *,
        id: str = None,
        connection_name: str = None,
        failure_detail: str = None,
        properties=None,
        **kwargs
    ) -> None:
        super(TokenExchangeInvokeResponse, self).__init__(**kwargs)
        self.id = id
        self.connection_name = connection_name
        self.failure_detail = failure_detail
        self.properties = properties


class TokenExchangeState(BaseModel):
    """TokenExchangeState

    :param connection_name: The connection name that was used.
    :type connection_name: str
    :param conversation: Gets or sets a reference to the conversation.
    :type conversation: ~microsoft.agents.protocols.models.ConversationReference
    :param relates_to: Gets or sets a reference to a related parent conversation for this token exchange.
    :type relates_to: ~microsoft.agents.protocols.models.ConversationReference
    :param bot_ur: The URL of the bot messaging endpoint.
    :type bot_ur: str
    :param ms_app_id: The bot's registered application ID.
    :type ms_app_id: str
    """

    connection_name: str = Field(None, alias="connectionName")
    conversation: ConversationReference = Field(None, alias="conversation")
    relates_to: ConversationReference = Field(None, alias="relatesTo")
    bot_url: str = Field(None, alias="botUrl")
    ms_app_id: str = Field(None, alias="msAppId")

    def __init__(
        self,
        *,
        connection_name: str = None,
        conversation=None,
        relates_to=None,
        bot_url: str = None,
        ms_app_id: str = None,
        **kwargs
    ) -> None:
        super(TokenExchangeState, self).__init__(**kwargs)
        self.connection_name = connection_name
        self.conversation = conversation
        self.relates_to = relates_to
        self.bot_url = bot_url
        self.ms_app_id = ms_app_id


class TokenRequest(BaseModel):
    """A request to receive a user token.

    :param provider: The provider to request a user token from
    :type provider: str
    :param settings: A collection of settings for the specific provider for
     this request
    :type settings: dict[str, object]
    """

    provider: str = Field(None, alias="provider")
    settings: dict = Field(None, alias="settings")

    def __init__(self, *, provider: str = None, settings=None, **kwargs) -> None:
        super(TokenRequest, self).__init__(**kwargs)
        self.provider = provider
        self.settings = settings


class TokenResponse(BaseModel):
    """A response that includes a user token.

    :param connection_name: The connection name
    :type connection_name: str
    :param token: The user token
    :type token: str
    :param expiration: Expiration for the token, in ISO 8601 format (e.g.
     "2007-04-05T14:30Z")
    :type expiration: str
    :param channel_id: The channelId of the TokenResponse
    :type channel_id: str
    """

    connection_name: str = Field(None, alias="connectionName")
    token: str = Field(None, alias="token")
    expiration: str = Field(None, alias="expiration")
    channel_id: str = Field(None, alias="channelId")

    def __init__(
        self,
        *,
        connection_name: str = None,
        token: str = None,
        expiration: str = None,
        channel_id: str = None,
        **kwargs
    ) -> None:
        super(TokenResponse, self).__init__(**kwargs)
        self.connection_name = connection_name
        self.token = token
        self.expiration = expiration
        self.channel_id = channel_id


class Transcript(BaseModel):
    """Transcript.

    :param activities: A collection of Activities that conforms to the
     Transcript schema.
    :type activities: list[~microsoft.agents.protocols.models.Activity]
    """

    activities: list[Activity] = Field(None, alias="activities")

    def __init__(self, *, activities=None, **kwargs) -> None:
        super(Transcript, self).__init__(**kwargs)
        self.activities = activities


class VideoCard(BaseModel):
    """Video card.

    :param title: Title of this card
    :type title: str
    :param subtitle: Subtitle of this card
    :type subtitle: str
    :param text: Text of this card
    :type text: str
    :param image: Thumbnail placeholder
    :type image: ~microsoft.agents.protocols.models.ThumbnailUrl
    :param media: Media URLs for this card. When this field contains more than
     one URL, each URL is an alternative format of the same content.
    :type media: list[~microsoft.agents.protocols.models.MediaUrl]
    :param buttons: Actions on this card
    :type buttons: list[~microsoft.agents.protocols.models.CardAction]
    :param shareable: This content may be shared with others (default:true)
    :type shareable: bool
    :param autoloop: Should the client loop playback at end of content
     (default:true)
    :type autoloop: bool
    :param autostart: Should the client automatically start playback of media
     in this card (default:true)
    :type autostart: bool
    :param aspect: Aspect ratio of thumbnail/media placeholder. Allowed values
     are "16:9" and "4:3"
    :type aspect: str
    :param duration: Describes the length of the media content without
     requiring a receiver to open the content. Formatted as an ISO 8601
     Duration field.
    :type duration: str
    :param value: Supplementary parameter for this card
    :type value: object
    """

    title: str = Field(None, alias="title")
    subtitle: str = Field(None, alias="subtitle")
    text: str = Field(None, alias="text")
    image: ThumbnailUrl = Field(None, alias="image")
    media: list[MediaUrl] = Field(None, alias="media")
    buttons: list[CardAction] = Field(None, alias="buttons")
    shareable: bool = Field(None, alias="shareable")
    autoloop: bool = Field(None, alias="autoloop")
    autostart: bool = Field(None, alias="autostart")
    aspect: str = Field(None, alias="aspect")
    duration: str = Field(None, alias="duration")
    value: object = Field(None, alias="value")

    def __init__(
        self,
        *,
        title: str = None,
        subtitle: str = None,
        text: str = None,
        image=None,
        media=None,
        buttons=None,
        shareable: bool = None,
        autoloop: bool = None,
        autostart: bool = None,
        aspect: str = None,
        duration: str = None,
        value=None,
        **kwargs
    ) -> None:
        super(VideoCard, self).__init__(**kwargs)
        self.title = title
        self.subtitle = subtitle
        self.text = text
        self.image = image
        self.media = media
        self.buttons = buttons
        self.shareable = shareable
        self.autoloop = autoloop
        self.autostart = autostart
        self.aspect = aspect
        self.duration = duration
        self.value = value


class AdaptiveCardInvokeAction(BaseModel):
    """AdaptiveCardInvokeAction.

    Defines the structure that arrives in the Activity.Value.Action for Invoke activity with
    name of 'adaptiveCard/action'.

    :param type: The Type of this Adaptive Card Invoke Action.
    :type type: str
    :param id: The Id of this Adaptive Card Invoke Action.
    :type id: str
    :param verb: The Verb of this Adaptive Card Invoke Action.
    :type verb: str
    :param data: The data of this Adaptive Card Invoke Action.
    :type data: dict[str, object]
    """

    type: str = Field(None, alias="type")
    id: str = Field(None, alias="id")
    verb: str = Field(None, alias="verb")
    data: dict = Field(None, alias="data")

    def __init__(
        self, *, type: str = None, id: str = None, verb: str = None, data=None, **kwargs
    ) -> None:
        super(AdaptiveCardInvokeAction, self).__init__(**kwargs)
        self.type = type
        self.id = id
        self.verb = verb
        self.data = data


class AdaptiveCardInvokeResponse(BaseModel):
    """AdaptiveCardInvokeResponse.

    Defines the structure that is returned as the result of an Invoke activity with Name of 'adaptiveCard/action'.

    :param status_code: The Card Action Response StatusCode.
    :type status_code: int
    :param type: The type of this Card Action Response.
    :type type: str
    :param value: The JSON response object.
    :type value: dict[str, object]
    """

    status_code: int = Field(None, alias="statusCode")
    type: str = Field(None, alias="type")
    value: dict = Field(None, alias="value")

    def __init__(
        self, *, status_code: int = None, type: str = None, value=None, **kwargs
    ) -> None:
        super(AdaptiveCardInvokeResponse, self).__init__(**kwargs)
        self.status_code = status_code
        self.type = type
        self.value = value


class AdaptiveCardInvokeValue(BaseModel):
    """AdaptiveCardInvokeResponse.

    Defines the structure that arrives in the Activity.Value for Invoke activity with Name of 'adaptiveCard/action'.

    :param action: The action of this adaptive card invoke action value.
    :type action: :class:`botframework.schema.models.AdaptiveCardInvokeAction`
    :param authentication: The TokenExchangeInvokeRequest for this adaptive card invoke action value.
    :type authentication: :class:`botframework.schema.models.TokenExchangeInvokeRequest`
    :param state: The 'state' or magic code for an OAuth flow.
    :type state: str
    """

    action: AdaptiveCardInvokeAction = Field(None, alias="action")
    authentication: TokenExchangeInvokeRequest = Field(None, alias="authentication")
    state: str = Field(None, alias="state")

    def __init__(
        self, *, action=None, authentication=None, state: str = None, **kwargs
    ) -> None:
        super(AdaptiveCardInvokeValue, self).__init__(**kwargs)
        self.action = action
        self.authentication = authentication
        self.state = state
