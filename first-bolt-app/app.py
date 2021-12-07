import os
from time import time
from connectAuto import funcMaquinas, qntDeMaquinasTotais
from insertAuto import enviarDados, pegarDados
from alerta import *
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler


# Initializes your app with your bot token and socket mode handler
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

# When a user joins the workspace, send a message in a predefined channel asking them to introduce themselves
@app.event("team_join")
def ask_for_introduction(event, say):
    welcome_channel = "alerts"
    user_id = event["user"]
    text = f"Welcome to the team, <@{user_id}>! 🎉 You can introduce yourself in this channel."
    say(text=text, channel=welcome_channel)

# Listens to incoming messages that contain "hello"
@app.message("start")
def message_hello(message, say):
    # say() sends a message to the channel where the event was triggered
    say(
        blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"Welcome to JETG3 <@{message['user']}>! Do you want to start the monitoring?"},
                "accessory": {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Start"},
                    "action_id": "button_click"
                }
            }
        ]
    )

    pegarDados()


@app.action("button_click")
def action_button_click(body, ack, say):
    # Acknowledge the action
    ack()
    say("Monitoramento iniciado... Em caso de anormalidade, seus alertas irão aparecer aqui:")
    while True:
        if(necessitaAlerta()):
            say(f"{enviarDados()}")
    


# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
