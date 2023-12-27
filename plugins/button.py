from config import FORCE_SUB_CHANNEL, FORCE_SUB_GROUP, FORCE_SUB_GROUP2, FORCE_SUB_GROUP3, FORCE_SUB_GROUP4, FORCE_SUB_GROUP5  

from pyrogram.types import InlineKeyboardButton


def start_button(client):
    if not FORCE_SUB_CHANNEL:
        if (
            not FORCE_SUB_GROUP
            and not FORCE_SUB_GROUP2
            and not FORCE_SUB_GROUP3
            and not FORCE_SUB_GROUP4
            and not FORCE_SUB_GROUP5
        ):
            return [
                [
                    InlineKeyboardButton(
                        text="• ᴛᴜᴛᴜᴘ •", callback_data="close"
                    ),
                ],
            ]
        if (
            FORCE_SUB_GROUP
            and FORCE_SUB_GROUP2
            and not FORCE_SUB_GROUP3
            and not FORCE_SUB_GROUP4
            and not FORCE_SUB_GROUP5
        ):
            return [
                [
                    InlineKeyboardButton(
                        text="ɢʀᴏᴜᴘ", url=client.invitelink2
                    ),
                    InlineKeyboardButton(
                        text="ᴄʜᴀɴɴᴇʟ", url=client.invitelink3
                    ),
                ],
                [
                    InlineKeyboardButton(
                        text="• ᴛᴜᴛᴜᴘ •", callback_data="close"
                    ),
                ],
            ]
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP and not FORCE_SUB_GROUP2 and not FORCE_SUB_GROUP3 and not FORCE_SUB_GROUP4 and not FORCE_SUB_GROUP5:
        return [
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close"),
            ],
        ]
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and not FORCE_SUB_GROUP2 and not FORCE_SUB_GROUP3 and not FORCE_SUB_GROUP4 and not FORCE_SUB_GROUP5:
        return [
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url=client.invitelink),
                InlineKeyboardButton(text="ɢʀᴏᴜᴘ", url=client.invitelink2),
            ],
            [InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close")],
        ]
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_GROUP2 and not FORCE_SUB_GROUP3 and not FORCE_SUB_GROUP4 and not FORCE_SUB_GROUP5:
        return [
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url=client.invitelink),
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url=client.invitelink3),
            ],
            [
                InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close"),
            ],
        ]
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_GROUP2 and FORCE_SUB_GROUP3 and not FORCE_SUB_GROUP4 and not FORCE_SUB_GROUP5:
        return [
            [
                InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink),
                InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink3),
                InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink4),
            ],
            [
                InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close"),
            ],
        ]
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_GROUP2 and FORCE_SUB_GROUP3 and FORCE_SUB_GROUP4 and not FORCE_SUB_GROUP5:
        return [
            [
                InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink),
                InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink3),
                InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink4),
            ],
            [
                InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink5),
            ],
            [
                InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close"),
            ],
        ]
    if (
        FORCE_SUB_CHANNEL
        and FORCE_SUB_GROUP
        and FORCE_SUB_GROUP2
        and FORCE_SUB_GROUP3
        and FORCE_SUB_GROUP4
    ):
        return [
            [
                InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink),
                InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink3),
                InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink4),
            ],
            [
                InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink5),
                InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink6),
            ],
            [
                InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close"),
            ],
        ]

def fsub_button(client, message):
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and not FORCE_SUB_GROUP2 and not FORCE_SUB_GROUP3 and not FORCE_SUB_GROUP4 and not FORCE_SUB_GROUP5:
        buttons = [
            [
                InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP and not FORCE_SUB_GROUP2 and not FORCE_SUB_GROUP3 and not FORCE_SUB_GROUP4 and not FORCE_SUB_GROUP5:
        buttons = [
            [
                InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=client.invitelink),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and not FORCE_SUB_GROUP2 and not FORCE_SUB_GROUP3 and not FORCE_SUB_GROUP4 and not FORCE_SUB_GROUP5:
        buttons = [
            [
                InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=client.invitelink),
                InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_GROUP2 and not FORCE_SUB_GROUP3 and not FORCE_SUB_GROUP4 and not FORCE_SUB_GROUP5:
        buttons = [
            [
                InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=client.invitelink),
                InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=client.invitelink3),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_GROUP2 and FORCE_SUB_GROUP3 and not FORCE_SUB_GROUP4 and not FORCE_SUB_GROUP5:
        buttons = [
            [
                InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=client.invitelink),
                InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=client.invitelink3),
                InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=client.invitelink4),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
             pass
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_GROUP2 and FORCE_SUB_GROUP3 and FORCE_SUB_GROUP4 and not FORCE_SUB_GROUP5:
        buttons = [
            [
                InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=client.invitelink),
                InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=client.invitelink3),
                InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=client.invitelink4),
            ],
            [
                InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=client.invitelink5),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if (
        FORCE_SUB_CHANNEL
        and FORCE_SUB_GROUP
        and FORCE_SUB_GROUP2
        and FORCE_SUB_GROUP3
        and FORCE_SUB_GROUP4
    ):
        buttons = [
            [
                InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=client.invitelink),
                InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=client.invitelink3),
                InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=client.invitelink4),
            ],
            [
                InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=client.invitelink5),
                InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=client.invitelink6),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons