from telethon import events
import random, re
from uniborg.util import admin_cmd

RUNSREACTS = [
    "`നിന്റെ നിഗമനം ശരിയാ... ഞാൻ അഹങ്കാരി 😎 തന്നെയാ..`",
    "`നാളത്തേയ്ക്ക് വേണ്ടിയുള്ള ഏറ്റവും നല്ല തയ്യാറെടുപ്പ് ഇന്ന് ഏറ്റവും നല്ലത് ചെയ്യുക എന്നുള്ളതാണ്..`",
    "`പലപ്പോഴും ഒന്നുമാഗ്രഹിക്കാതെ കൂടെ നിൽക്കുന്നവരെ നമ്മൾ പരിഗണിക്കാറുപോലുമില്ല..കാരണം അവർ നിങ്ങളെ സ്നേഹിക്കുന്നുവെന്ന് അഭിനയിക്കുകയല്ല. അവസരം കാത്ത് മറഞ്ഞിരിക്കുകയല്ല. ഒരുവിധേനയും ശല്ല്യം ചെയ്യുന്നില്ല.. ഒന്ന് കാലിടറിയാൽ ചേർത്ത് പിടിക്കാൻ ആദ്യമെത്തുക ആ കരങ്ങളായിരിക്കും..`",
    "`ചിലന്തിയും മനുഷ്യനും ഒരുപോലെയാണ് കാരണം, രണ്ടും അധികനേരം നെറ്റിൽ ആണ് `",
    "`നിങ്ങൾ മഴവെളളമായി ഇറ്റിറ്റു വീണു കൊണ്ടേയിരിക്കുക. ഒരിക്കൽ ലക്ഷ്യത്തിന്റെ പാറ കുഴിയുക തന്നെ ചെയ്യും..`",
    "`ഞങ്ങൾ അധോലോകക്കാർ കറയാറില്ല  ... സങ്കടം വരുമ്പോൾ AK 47 എടുത്തു ആകാശത്തേയ്ക്ക് നലഞ്ചു വട്ടം വെടി വെക്കും ...🕺🏻 ആ  പിഷ്ക്കും🔫🔫..`",
    "`പഞ്ചസാരയ്ക്കും ഉപ്പിനും ഒരേ നിറമാണ്💙....പക്ഷെ,രണ്ടിനും😋 രുചി വളരെ വ്യത്യസ്തമാണ്...അതുപോലെയാണ് ചില സുഹൃത്ത് ബന്ധങ്ങളും ..`",
    "`ഒര് കഥ സൊല്ലട്ടുമാ സാര്....മഴയെ ത്യേച്ച് കാറ്റിന്റെ കൂടെ പോയ കറണ്ടിന്റെ ഗഥ..😑😑💔 ”`",
    "👦തല പോയാലും 😭കരയില്ല..!! 🙁 ഞങ്ങൾ 👤ആൺകുട്ടികൾ 😭കരയാറില്ല.... 😂💪 .`",
    "`ഇത്രേം കാലം എവിടെ ആയിരുന്നു....!🥰 `",
]

@borg.on(admin_cmd(pattern="odra"))
async def _(event):
    if event.fwd_from:
         return
    bro = random.randint(0, len(RUNSREACTS) - 1)    
    reply_text = RUNSREACTS[bro]
    await event.edit(reply_text)
