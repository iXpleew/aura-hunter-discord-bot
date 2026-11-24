from database import get_messages_for_manual_classification, get_username_by_id


def manual_evaluating_messages(messages: list):
    # 0 - Ultra negative, 1 - negative, 2 - neutral, 3 - positive, 4 - ultra positive
    messages_with_aura = {}
    for message in messages_list:
        print(f"{get_username_by_id(message.user_id)} typed: {message.content}")
        score = int(input("Enter aura classification: "))
        messages_with_aura[message] = score

    return messages_with_aura


if __name__ == "__main__":
    messages_list: list = get_messages_for_manual_classification()
    messages_aura_points = manual_evaluating_messages(messages_list)