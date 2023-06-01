# PROPOSAL

## FOREIGN LANGUAGE TUTOR CHATBOT

### OVERVIEW
The foreign language tutor app leverages the OpenAI API to generate lifelike conversation scenarios, allowing language learners to practice their skills in immersive contexts, save conversations and vocabulary for future review for a personalized language learning experience.
### GOALS
The goal of this website is to provide language learners with a user friendly platform to develop and improve their conversational skills through immersive conversation scenarios with a foreign language chatbot tutor.
### TARGET USERS
Intermediate to advanced language learners who want to enhance their conversational skills will get the most out of the app, although beginners with some knowledge of their target language could still benefit.
### DATA
This app will utilize the OpenAI API to generate conversation scenarios. The specific data requirements would involve sending text prompts to the API and receiving generated responses. The app will also incorporate user data such as previous conversations and selected vocabulary.
### APPROACH
#### Database Schema
Tables for user authentication/authorization, storing user profiles and preferences, saved conversations, and vocabulary lists.
![databaseschema](/static/images/drawSQL-foreign-language-tutor-export-2023-06-01.png)
#### API Issues
Potential issues with the OpenAI API could include rate limits, handling API errors and responses. 
#### Functionality
User registration and login. Users can create new chat bots based on their language preference, level of proficiency, and conversation topic preferences. The app will generate lifelike conversations for users to practice their language skills. Users will be able to view save their chats and access saved conversations along with selected vocabulary for review.
### USER FLOW
1. Login/Sign up
2. User homepage to create a new chat bot, set preferences, view previous chats
3. Chat page where users interact with the chat bot
### FEATURES BEYOND CRUD
Personalization: Users can customize their chat bots based on language preferences, proficiency level preferences, and conversational preferences. The app generates conversation scenarios tailored to each user's preferences, providing a personalized language learning experience.
### STRETCH GOALS
1. A flashcard creation feature that allows users to generate flashcards from vocabulary lists saved during conversations, enabling them to reinforce their language learning by reviewing and practicing key words and phrases in a structured manner.
2. Extend the customization options for chat bots to include additional conversational styles, such as formal or colloquial language.
