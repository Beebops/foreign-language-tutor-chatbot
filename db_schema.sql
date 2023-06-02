-- Exported from https://drawsql.app/teams/

CREATE TABLE "chat_log"(
    "id" INTEGER NOT NULL,
    "user/bot" VARCHAR(255) NOT NULL,
    "text" TEXT NOT NULL,
    "created_at" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL,
    "chats_id" INTEGER NOT NULL
);
ALTER TABLE
    "chat_log" ADD PRIMARY KEY("id");
CREATE INDEX "chat_log_chats_id_index" ON
    "chat_log"("chats_id");
CREATE TABLE "chats"(
    "id" INTEGER NOT NULL,
    "user_id" INTEGER NOT NULL,
    "text" TEXT NOT NULL,
    "language_level" INTEGER NULL,
    "language" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "chats" ADD PRIMARY KEY("id");
CREATE INDEX "chats_user_id_index" ON
    "chats"("user_id");
CREATE TABLE "users"(
    "id" INTEGER NOT NULL,
    "username" VARCHAR(255) NOT NULL,
    "password" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "users" ADD PRIMARY KEY("id");
ALTER TABLE
    "chat_log" ADD CONSTRAINT "chat_log_chats_id_foreign" FOREIGN KEY("chats_id") REFERENCES "chats"("id");
ALTER TABLE
    "chats" ADD CONSTRAINT "chats_user_id_foreign" FOREIGN KEY("user_id") REFERENCES "users"("id");