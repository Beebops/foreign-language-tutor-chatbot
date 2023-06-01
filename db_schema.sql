-- Exported from https://drawsql.app/teams/

CREATE TABLE "chats_words"(
    "id" INTEGER NOT NULL,
    "chat_id" INTEGER NOT NULL,
    "word_id" INTEGER NOT NULL
);
ALTER TABLE
    "chats_words" ADD PRIMARY KEY("id");
CREATE INDEX "chats_words_chat_id_index" ON
    "chats_words"("chat_id");
CREATE INDEX "chats_words_word_id_index" ON
    "chats_words"("word_id");
CREATE TABLE "users_words"(
    "id" INTEGER NOT NULL,
    "user_id" INTEGER NOT NULL,
    "word_id" INTEGER NOT NULL
);
ALTER TABLE
    "users_words" ADD PRIMARY KEY("id");
CREATE INDEX "users_words_user_id_index" ON
    "users_words"("user_id");
CREATE INDEX "users_words_word_id_index" ON
    "users_words"("word_id");
CREATE TABLE "chats"(
    "id" INTEGER NOT NULL,
    "user_id" INTEGER NOT NULL,
    "text" TEXT NOT NULL,
    "english_translation" TEXT NOT NULL,
    "language_level" INTEGER NULL
);
ALTER TABLE
    "chats" ADD PRIMARY KEY("id");
CREATE INDEX "chats_user_id_index" ON
    "chats"("user_id");
CREATE TABLE "users"(
    "id" INTEGER NOT NULL,
    "username" VARCHAR(255) NOT NULL,
    "password" VARCHAR(255) NOT NULL,
    "language_learning" VARCHAR(255) NULL,
    "language_level" INTEGER NULL
);
ALTER TABLE
    "users" ADD PRIMARY KEY("id");
CREATE TABLE "words"(
    "id" INTEGER NOT NULL,
    "word" TEXT NOT NULL,
    "english_translation" TEXT NOT NULL,
    "language" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "words" ADD PRIMARY KEY("id");
ALTER TABLE
    "users_words" ADD CONSTRAINT "users_words_user_id_foreign" FOREIGN KEY("user_id") REFERENCES "users"("id");
ALTER TABLE
    "users_words" ADD CONSTRAINT "users_words_word_id_foreign" FOREIGN KEY("word_id") REFERENCES "words"("id");
ALTER TABLE
    "chats_words" ADD CONSTRAINT "chats_words_chat_id_foreign" FOREIGN KEY("chat_id") REFERENCES "chats"("id");
ALTER TABLE
    "chats" ADD CONSTRAINT "chats_user_id_foreign" FOREIGN KEY("user_id") REFERENCES "users"("id");
ALTER TABLE
    "chats_words" ADD CONSTRAINT "chats_words_word_id_foreign" FOREIGN KEY("word_id") REFERENCES "words"("id");