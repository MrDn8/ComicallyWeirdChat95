# ULTRA SMART AI DOCS CHATROOM - RETRO WHITE UI STYLE

import tkinter as tk
from tkinter import simpledialog
import random

# ---------------- WINDOW ----------------

root = tk.Tk()
root.title("ComicallyWeirdChat95")
root.attributes("-fullscreen", True)

# lighter retro white background
root.configure(bg="#efefef")

# ---------------- COLORS ----------------

colors = [
    "red","blue","green","purple","orange","pink",
    "brown","cyan","magenta","gold","lime","navy",
    "turquoise","violet","black","gray","maroon",
    "darkgreen","deepskyblue","crimson","indigo",
    "salmon","teal","coral","darkorange","hotpink",
    "skyblue","yellowgreen","dodgerblue","orchid",
    "slateblue","tomato","springgreen","royalblue"
]

# ---------------- THEME COLOR ----------------

theme_color = random.choice(colors)

# ---------------- USERNAME ----------------

username = simpledialog.askstring("Username", "Enter your username:")

if not username:
    username = "NoName"

# ---------------- TOP BAR ----------------

topbar = tk.Frame(
    root,
    bg=theme_color,
    height=38,
    relief="raised",
    bd=2
)

topbar.pack(fill="x")

tk.Label(
    topbar,
    text="ComicallyWeirdChat95",
    font=("Helvetica", 12),
    bg=theme_color
).pack(side="left", padx=15, pady=8)

tk.Label(
    topbar,
    text=f"Logged in as: {username}",
    font=("Helvetica", 9),
    bg=theme_color,
    fg="black"
).pack(side="right", padx=15)

# ---------------- TOOLBAR ----------------

toolbar = tk.Frame(
    root,
    bg=theme_color,
    height=32,
    relief="raised",
    bd=2
)

toolbar.pack(fill="x")

toolbar_buttons = ["Docs", "Files", "Printer", "✂", "???"]

for icon in toolbar_buttons:

    tk.Button(
        toolbar,
        text=icon,
        font=("Helvetica", 9),
        width=3,
        bg=theme_color,
        relief="flat",
        bd=1,
        activebackground=theme_color
    ).pack(side="left", padx=2, pady=2)

# ---------------- MAIN AREA ----------------

outer_frame = tk.Frame(root, bg="#f2f2f2")
outer_frame.pack(fill="both", expand=True)

doc_frame = tk.Frame(
    outer_frame,
    bg="#fcfcfc",
    width=920,
    height=670,
    relief="sunken",
    bd=2
)

doc_frame.place(relx=0.5, rely=0.5, anchor="center")

# ---------------- CHAT BOX ----------------

chat_box = tk.Text(
    doc_frame,
    bg="#ffffff",
    fg="black",
    font=("Helvetica", 11),
    wrap="word",
    relief="flat",
    bd=0,
    padx=8,
    pady=8,
    insertbackground="black"
)

chat_box.place(relwidth=1, relheight=0.88)

# ---------------- INPUT ----------------

bottom_frame = tk.Frame(
    doc_frame,
    bg=theme_color,
    relief="raised",
    bd=2
)

bottom_frame.place(rely=0.88, relwidth=1, relheight=0.12)

entry = tk.Entry(
    bottom_frame,
    font=("Helvetica", 11),
    bg="white",
    relief="sunken",
    bd=2
)

entry.place(relx=0.02, rely=0.2, relwidth=0.78, relheight=0.6)

# ---------------- BOT NAMES ----------------

bots = [
    "Pentale","CoolKid","User4","Shadow","PixelGuy","RoyIsCool",
    "n00b","Guest123","VoidWalker","XxDarkWolfxX","ClassicBlox",
    "BlockyDude","Neon","Conner46","EpicGuest","MrBuilder",
    "TurboBlox","SnakeByte","WaveRunner","Ghost","PizzaLord",
    "SpeedRunner","FireIsBad","Error404","MoonWalker","GlitchKid",
    "TinyBuilder","RainbowUser","BrickMaster","CloudPlayer",
    "Bytebot","V4MP","OmegaCube","NightPlayer","CyberGirl",
    "ChillDude","LavaCube","Nova","SleepyStar","IceWalker"
]

# ---------------- STORAGE ----------------

message_count = 0
recent_messages = []

# ---------------- ADD MESSAGE ----------------

def add_message(user, msg):

    global message_count

    color = random.choice(colors)

    tag = f"msg{message_count}"

    message_count += 1

    chat_box.insert("end", f"[{user}]: {msg}\n", tag)

    chat_box.tag_config(tag, foreground=color)

    chat_box.see("end")

    if message_count > 2000:
        chat_box.delete("1.0", "50.0")

    recent_messages.append((user, msg.lower()))

    if len(recent_messages) > 40:
        recent_messages.pop(0)

# ---------------- SMART AI RESPONSE ----------------

def generate_ai_response(msg):

    msg = msg.lower()

    if any(w in msg for w in ["hello","hi","hey","yo","sup"]):
        return random.choice(["yo","hey","wassup","hi lol","what's good","yo chat","eyy"])

    elif "shut up" in msg:
        return random.choice([
            "nah you shut up",
            "jeez lol",
            "make me",
            "someone getting spicy >_>",
            "yo shut yo ass up"
        ])

    elif "minecraft" in msg:
        return random.choice([
            "Minecraft is forever elite",
            "creepers still scare me ngl",
            "old Minecraft > everything",
            "bro I miss 2013 survival worlds",
            "diamond hunting was peak stress",
            "I, AM STEVE"
        ])

    elif "tiktok" in msg:
        return random.choice([
            "tiktok got mad funny vids",
            "my tiktok account is has 12.7k followers : 3",
            "tiktok weird people on there",
            "my tiktok fyp is washed",
            "yall be doomscrolling?"
        ])

    elif any(w in msg for w in ["skibidi","rizz","sigma","gyatt","aura","ohio"]):
        return random.choice([
            "bro is speaking pure brainrot ",
            "what does that even mean anymore",
            "internet language is evolving too fast",
            "here it comes the toddlers",
            "bro genuinely laughs at that shi"
        ])

    elif "school" in msg:
        return random.choice([
            "school is lowkey pain",
            "bro I need summer back",
            "nah becuase why school just like prison",
            "school food be taking notes from arby's",
            "teachers got no chill sometimes"
        ])

    elif any(w in msg for w in ["fuck","shit","damn","bitch","ass"]):
        return random.choice([
            "oooooooooooo",
            "someone gettin maddd XD",
            "do i hear drama >:)",
            "chill gng",
            "you good?"
        ])

    elif "fornite" in msg or "fortnite" in msg:
        return random.choice([
            "Fortnite was peak 2018 vibes",
            "default dancing era was crazy",
            "bro still dropping tilted towers references",
            "build battles used to be insane",
            "I miss old Fortnite lobbies"
        ])

    elif any(w in msg for w in ["goodbye","bye","cya","goodnight","gn"]):
        return random.choice([
            "cya bro","goodnight","bye lol","see you later","later",
            "dont disappear forever","peace","gn chat"
        ])

    elif any(w in msg for w in ["67","brainrot"]):
        return random.choice([
            "average brainrot survivor",
            f"{username} watches 12 hour brainrot meme compilations",
            "tiktok destroyed your attention span",
            "you definitely say skibidi unironically",
            "bro is cooked",
            "your humor is beyond repair",
            "most sane internet user",
            "terminally online behavior",
            "actual brainless dialogue",
            f"seek grass immediately {username}"
        ])

    elif "roblox" in msg:
        return random.choice([
            "old roblox was peak",
            "i miss tix :(",
            "builderman era was crazy",
            "classic roblox > modern",
            "roblox music was fire"
        ])

    elif any(w in msg for w in ["game","play","gaming"]):
        return random.choice([
            "W game","this is actually fun","im addicted now",
            "lowkey good","better than expected","gaming vibes"
        ])

    elif any(w in msg for w in ["lol","lmao","haha"]):
        return random.choice(["💀","nah that's wild","bro WHAT","im dead","LOL","real talk"])

    elif any(w in msg for w in ["python","code","script","coding"]):
        return random.choice([
            "coding at 3am moment",
            "python is cool but buggy",
            "errors ruin everything",
            "respect the grind",
            "debugging pain"
        ])

    elif any(w in msg for w in ["pizza","food","burger","eat"]):
        return random.choice([
            "now I'm hungry","pizza is elite","W food take",
            "same honestly","bro got taste"
        ])

    elif any(w in msg for w in ["music","song","breakcore"]):
        return random.choice([
            "breakcore goes crazy",
            "music is carrying this chat",
            "what song is that?",
            "fire taste",
            "depends on mood"
        ])

    elif any(w in msg for w in ["sad","cry","depressed","upset"]):
        return random.choice([
            "damn that sucks","hope it gets better","stay strong","rip","that’s rough"
        ])

    elif "?" in msg:
        return random.choice(["probably","idk tbh","maybe","depends","not sure","could be"])

    elif "!" in msg:
        return random.choice([":O","WHAT","OMG","nah ts crazy"])

    elif "arby's" in msg:
        return random.choice([
            "arby's is ahh",
            "who genuinely eats arby's",
            "one bite of arby's can kill you",
            "arby's..THAT SHIT SOUND NASTY AF"
        ])

    elif any(w in msg for w in ["no","nah","wrong"]):
        return random.choice([
            "nah I disagree","you're tripping","hard disagree",
            "not sure about that one","false"
        ])

    else:
        return random.choice([
            "real","facts","true","interesting","bro what",
            "makes sense","W","lowkey true","kinda agree","noted"
        ])

# ---------------- BOT RESPONSE ----------------

def bot_reply(original_user, original_msg, depth=0):

    if depth > 3:
        return

    bot = random.choice(bots)

    while bot == original_user:
        bot = random.choice(bots)

    response = generate_ai_response(original_msg)

    add_message(bot, response)

    if random.randint(1, 100) < 55:

        root.after(
            max(700, len(response) * 45),
            lambda b=bot, r=response, d=depth+1: bot_reply(b, r, d)
        )

# ---------------- SEND MESSAGE ----------------

def send_message(event=None):

    msg = entry.get().strip()

    if not msg:
        return

    add_message(username, msg)

    entry.delete(0, "end")

    for i in range(random.randint(2, 5)):

        root.after(
            random.randint(600, 2000) * (i + 1),
            lambda m=msg: bot_reply(username, m)
        )

# ---------------- RANDOM CHAT ----------------

random_topics = [
    "anyone here","this chat is chaotic","old roblox was better",
    "who remembers the freeze trend in 2016","im bored","W chat",
    "coding at 3am","breakcore hits different","windows 95 vibes",
    "someone say something","this feels nostalgic","lol",
    "brainrot is kinda funny","free RoyIsCool","SUB TO MrDn8",
    "BOGGLE sounds good rn","67","pizza sounds yummy rn",
    "bruh gta 6 never releasing","i don't have friends, i got family",
    "<0>","pluh","arby's for life","hot cheeto girls genuinely disgust me",
    "EVERYONE SHUT UP","yall tryna hop on fortnite?",
    "damn bro i got school tomorrow",
    "roblox now is just straight up ass",
    "MINECRAFT NEEDS A END UPDATE"
]

def random_chat():

    if random.randint(1, 100) < 70:

        bot = random.choice(bots)

        if recent_messages and random.randint(1, 100) < 70:
            _, recent = random.choice(recent_messages)
            msg = generate_ai_response(recent)
        else:
            msg = random.choice(random_topics)

        add_message(bot, msg)

        if random.randint(1, 100) < 50:

            root.after(
                random.randint(1000, 3000),
                lambda b=bot, m=msg: bot_reply(b, m)
            )

    root.after(2200, random_chat)

# ---------------- SEND BUTTON ----------------

tk.Button(
    bottom_frame,
    text="Send. Duh",
    font=("Helvetica", 10),
    bg=theme_color,
    fg="black",
    relief="raised",
    bd=2,
    activebackground=theme_color,
    command=send_message
).place(relx=0.82, rely=0.2, relwidth=0.16, relheight=0.6)

entry.bind("<Return>", send_message)

# ---------------- EXIT ----------------

root.bind("<Escape>", lambda e: root.attributes("-fullscreen", False))

# ---------------- START ----------------

chat_box.insert(
    "end",
    "Welcome to RandomChatroom95 (Koza was here)\n\n",
    "w"
)

chat_box.tag_config("w", foreground="gray")

random_chat()

root.mainloop()