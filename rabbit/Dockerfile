FROM rabbitmq:3.6-alpine

ADD ./rabbitmq.config /etc/rabbitmq/rabbitmq.config
ADD ./enabled_plugins /etc/rabbitmq/enabled_plugins

ENV RABBITMQ_ERLANG_COOKIE="atata"
