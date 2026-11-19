from database import get_messages_for_manual_classification, get_username_by_id


def manual_evaluating_messages(messages: list):
    pass


if __name__ == "__main__":
    messages_list: list = get_messages_for_manual_classification()
    for message in messages_list:
        print(f"{get_username_by_id(message.user_id)} typed: {message.content}")
