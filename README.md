Chatbot for Personalized Learning

This repository contains the source code and configuration files for a Rasa-based chatbot designed for personalized learning experiences. The chatbot uses natural language understanding (NLU) and dialogue management to engage users and provide customized educational content.

Project Structure

actions/: Contains custom Python actions to extend the chatbot's functionality.

data/: Includes training data for NLU and dialogue management:

nlu.yml: Contains examples for intent classification and entity extraction.

stories.yml: Defines conversational flows.

rules.yml: Specifies rules for specific chatbot behaviors.

tests/: Contains tests to validate the chatbot's behavior.

config.yml: Configures the NLU pipeline and policies for dialogue management.

credentials.yml: Sets up credentials for communication channels like Slack, Facebook Messenger, etc.

domain.yml: Defines intents, entities, slots, responses, forms, and actions.

endpoints.yml: Configures the action server and tracker store endpoints.

requirements.txt: Lists the Python dependencies required to run the project.

Prerequisites

Python 3.8 or higher

Rasa (see requirements.txt for exact versions)

Optional: Docker (for deployment)

Installation

Clone this repository:

git clone https://github.com/your_username/chatbot_for_personalized_learning.git
cd chatbot_for_personalized_learning

Create a virtual environment and activate it:

python3 -m venv venv
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Usage

Training the Model

Train the chatbot's NLU and dialogue models:

rasa train

Running the Chatbot

Start the action server (for custom actions):

rasa run actions

Start the Rasa server:

rasa run

Interact with the bot in the terminal:

rasa shell

Running Tests

Validate the chatbot using the test stories:

rasa test

Deployment

To deploy the chatbot, you can use:

Docker: Create Docker images for the Rasa server and action server.

Cloud Platforms: Deploy on platforms like AWS, GCP, or Azure.

Customization

Update the domain.yml file to add new intents, responses, or slots.

Add or modify training examples in the data/nlu.yml file.

Define new conversational flows in data/stories.yml.

Extend functionality by adding custom actions in the actions/ directory.

Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments

Rasa for providing the framework.

Open-source contributors for their support and tools.
 
