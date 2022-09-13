{% for message in previous_messages %}
{% if message['is_my_message'] %}Me{% else %}Them{% endif %}: {{ message['text'] }}
{% endfor %}