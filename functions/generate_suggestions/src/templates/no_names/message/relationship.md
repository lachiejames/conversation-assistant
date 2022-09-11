{% for message in previous_messages %}
{% if message['is_my_message'] %}Me{% else %}{{ their_relationship_to_me }}{% endif %}: {{ message['text'] }}
{% endfor %}