from database import *


def manual_evaluating_messages(messages: list) -> dict:
    # 0 - Ultra negative, 1 - negative, 2 - neutral, 3 - positive, 4 - ultra positive
    messages_with_aura = {}
    for message in messages:
        print(f"{get_username_by_id(message.user_id)} typed: {message.content}")
        score = int(input("Enter aura classification: "))
        messages_with_aura[message.id] = score

    return messages_with_aura


def automatic_evaluating_message(messages: list, aura_class: int) -> dict:
    messages_with_aura = {}
    for message in messages:
        messages_with_aura[message.id] = aura_class

    return messages_with_aura


if __name__ == "__main__":
    messages_list: list = get_specific_messages("nie bieg")
    mess_dict = automatic_evaluating_message(messages_list, 0)
    insert_aura_messages(mess_dict, "automatic")
