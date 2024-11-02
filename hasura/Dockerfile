FROM hasura/graphql-engine:v2.44.0.cli-migrations-v3

ADD ./metadata /hasura-metadata
ADD ./migrations /hasura-migrations

# 接收构建参数
ARG VERSION_HISTORY_JSON
ADD ${VERSION_HISTORY_JSON} ./version_history.json