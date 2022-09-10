{% for message in previous_messages %}
{% if message['is_my_message'] %}{{ my_name }}{% else %}{{ their_name }}{% endif %}: {{ message['text'] }}
{% endfor %}