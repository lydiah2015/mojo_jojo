import dialogflow
import os

class DialogFlowHandler:

    def __init__(self):
        self.session_client = dialogflow.SessionsClient()

    def detect_user_intent(self, text, language_code="en",project_id=None,session_id=None):
        if project_id == None:project_id=os.getenv('DIALOGFLOW_PROJECT_ID')
        if session_id==None:session_id="unique"
        session = self.session_client.session_path(project_id, session_id)
        if text:
            text_input = dialogflow.types.TextInput(
                text=text, language_code=language_code
                )
            query_input = dialogflow.types.QueryInput(text=text_input)
            response = self.session_client.detect_intent(
                session=session, query_input=query_input
                )
            return response.query_result.fulfillment_text
        return False
