from os import getenv
from dotenv import load_dotenv

load_dotenv()

get_queue = {}


API_ID = 19588819
API_HASH = "e8e174181134c5991f20cc6bf9f55bf1"

ASS_HANDLER = list(getenv("ASS_HANDLER", ".").split())
BOT_TOKEN = "5787903173:AAG5WoVWgjbKEPJVksApcLIHVvqXaxt6ksk"

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "150"))
LOGGER_ID = -1001851312811
MONGO_DB_URI = "mongodb+srv://musicwala:musicwalala@cluster0.svyk5ce.mongodb.net/?retryWrites=true&w=majority"
OWNER_ID = 1890206319

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/dd943dd5f2266887b1781.jpg")
START_IMG = "https://te.legra.ph/file/6abbc675ced4e45254464.jpg"

SUPPORT_CHAT = "https://t.me/sidekickfriend"
SUPPORT_CHANNEL = " https://t.me/ikku_hoi "

STRING_SESSION = "AQB1L1chKxal7jEz7qblDbDtBnbRikKlBXRPCevQ4JA_663eUanfSjinm9xXOPqOfEIpx17O5hrwFVac7--eE-k_ShRvhhy4Ln3y1XzGpDKa2SOlxv-2k3sNOnUuXeGu3hBVro-ECWFvGX8FVFwMP_-qzYEy-tZ2MxOTbsFnmZO9CmaQlb3OefEw_eboeOJctfH2a4nHovPHsOIc03aNpRBTEBgtH43bV1ruBEmrmFIts_o3qEBiC0V05KO-almLXv4w51Kc3fp2DD2x5Hg27Czb8IXpA-ZrWnyHgNVe0R3GxNV3HCbRScBWHEzwnKokr8qSUooB0oiYSvz_yqaY8XAiAAAAAUBH-IgA"
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
