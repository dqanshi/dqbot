""" Sing a Malayalam song... 
    Command .se 
    By @Deonnn """



# BY @Deonnn

from telethon import events

import asyncio

import os

import sys

import random



@borg.on(events.NewMessage(pattern=r"\.seng", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    await event.edit("Singing...singing.... singing....singing...🎶💃🎶.")

    await asyncio.sleep(2)

    x=(random.randrange(1,33))

    if x==1:

        await event.edit("🎶 ഒരുനാൾ തരളമിവനിൽ... പടരൂ വനലതികയായ്... മുറുകെ... മതിവരുവോളം സഖീ... 🎶")

    if x==2:

        await event.edit("🎶 അഴലിന്റെ ആഴങ്ങളിൽ അവൾ മാഞ്ഞുപോയ്... നോവിന്റെ തീരങ്ങളിൽ ഞാൻ മാത്രമായ്... 🎶")

    if x==3:

        await event.edit("🎶 ആവണിപ്പൊന്നൂഞ്ഞാലാടിക്കാം നിന്നെ ഞാൻ... ആയില്ല്യം കാവിലെ വെണ്ണിലാവേ... 🎶")

    if x==4:

        await event.edit("🎶 ഇന്ദ്രനീലിമയോലും ഈ മിഴി പൊയ്കകളിൽ... ഇന്നലെ നിൻ മുഖം നീ നോക്കി നിന്നൂ... 🎶")

    if x==5:

        await event.edit("🎶 മയിലായ് പറന്നുവാ മഴവില്ലു തോൽക്കുമെന്നഴകേ... 🎶")

    if x==6:

        await event.edit("🎶 നിലാവിന്റെ നീലഭസ്മ കുറിയണിഞ്ഞവളേ... കാതിലോലക്കമ്മലിട്ടു കുണുങ്ങി നിന്നവളേ... 🎶")

    if x==7:

        await event.edit("🎶 നീയൊരു പുഴയായ് തഴുകുമ്പോൾ ഞാൻ പ്രണയം വിടരും കരയാവും... 🎶")    

    if x==8:

        await event.edit("🎶 അരികിൽ നീയുണ്ടായിരുന്നെങ്കിലെന്നു ഞാൻ... ഒരുമാത്ര വെറുതേ നിനച്ചുപോയി... 🎶")

    if x==9:

        await event.edit("🎶 എത്രയോ ജന്മമായ് നിന്നെഞാൻ തേടുന്നു... അത്രമേൽ ഇഷ്ടമായ് നിന്നെയെൻ പുണ്യമേ... 🎶")

    if x==10:

        await event.edit("🎶 മഴത്തുള്ളികൾ പൊഴിഞ്ഞീടുമീ നാടൻ വഴി... നനഞ്ഞോടിയെൻ കുടക്കീഴിൽ നീ വന്ന നാൾ... 🎶")
     
    if x==11:

        await event.edit("🎶 കരളേ നിൻ കൈ പിടിച്ചാൽ, കടലോളം വെണ്ണിലാവ്... ഉൾക്കണ്ണിൻ കാഴ്ചയിൽ നീ, കുറുകുന്നൊരു വെൺപിറാവ്... 🎶")

    if x==12:

        await event.edit("🎶 മറന്നിട്ടുമെന്തിനോ മനസ്സിൽ തുളുമ്പുന്നു മൗനാനുരാഗത്തിൻ ലോലഭാവം... 🎶")
    
    if x==13:

        await event.edit("🎶 മഴക്കാലം എനിക്കായി മയിൽ ചെലുള്ള പെണ്ണേ നിന്നെത്തന്നേ... 🎶")

    if x==14:

        await event.edit("🎶 മിഴിയറിയാതെ വന്നു നീ മിഴിയൂഞ്ഞാലിൽ... കനവറിയാതെയേതോ കിനാവു പോലെ... 🎶")
        
    if x==15:

        await event.edit("🎶 ചന്ദനച്ചോലയിൽ മുങ്ങിനീരാടിയെൻ ഇളമാൻ കിടാവേ ഉറക്കമായോ... 🎶")

    if x==16:

        await event.edit("🎶 കറുത്തപെണ്ണേ നിന്നെ കാണാഞ്ഞിട്ടൊരു നാളുണ്ടേ... 🎶")
     
    if x==17:

        await event.edit("🎶 താമരപ്പൂവിൽ വാഴും ദേവിയല്ലോ നീ... പൂനിലാക്കടവിൽ പൂക്കും പുണ്യമല്ലോ നീ... 🎶")

    if x==18:

        await event.edit("🎶 പാടം പൂത്തകാലം പാടാൻ വന്നു നീയും... 🎶")

    if x==19:

        await event.edit("🎶 രാജഹംസമേ മഴവിൽ കുടിലിൽ... സ്നേഹദൂതുമായ് വരുമോ... 🎶")

    if x==20:

        await event.edit("🎶 പത്തുവെളുപ്പിന് മുറ്റത്തു നിക്കണ കസ്തൂരി മുല്ലയ്ക്ക് കാത്തുകുത്ത്... എന്റെ കസ്തൂരി മുല്ലയ്ക്ക് കാത്തുകുത്ത്... 🎶")

    if x==21:
        
        await event.edit("🎶 മഞ്ഞൾ പ്രസാദവും നെറ്റിയിൽ ചാർത്തി... മഞ്ഞക്കുറിമുണ്ടു ചുറ്റി... 🎶")
        
    if x==22:
        
        await event.edit("🎶 അന്തിപ്പൊൻവെട്ടം കടലിൽ മെല്ലെത്താഴുമ്പോൾ... മാനത്തെ മുല്ലത്തറയില് മാണിക്യച്ചെപ്പ്... 🎶")
       
    if x==23:

        await event.edit("🎶 അമ്പലപ്പുഴെ ഉണ്ണിക്കണ്ണനോടു നീ... എന്തുപരിഭവം മെല്ലെയോതിവന്നുവോ... 🎶")

    if x==24:

        await event.edit("🎶 കുടജാദ്രിയിൽ കുടചൂടുമാ കോടമഞ്ഞുപോലെയീ പ്രണയം... തഴുകുന്നു, എന്നെ പുണരുന്നു... 🎶")

    if x==25:
        
        await event.edit("🎶 ശ്യാമാംബരം പുൽകുന്നൊരാ വെൺചന്ദ്രനായ് നിൻ പൂമുഖം... 🎶")
        
    if x==26:
        
        await event.edit("🎶 ശ്രീരാഗമോ തേടുന്നിതെൻ വീണതൻ പൊൻ തന്ത്രിയിൽ... 🎶")
        
    if x==27:
        
        await event.edit("🎶 എന്തിനു വേറൊരു സൂര്യോദയം... നീയെൻ പൊന്നുഷസ്സന്ധ്യയല്ലേ... 🎶")
        
    if x==28:
        
        await event.edit("🎶 അനുരാഗിണീ ഇതായെൻ കരളിൽ വിരിഞ്ഞ പൂക്കൾ... 🎶")

    if x==29:
        
        await event.edit("🎶 പാടാം നമുക്കു പാടാം... വീണ്ടുമൊരു പ്രേമഗാനം... 🎶")
        
    if x==30:
        
        await event.edit("🎶 അല്ലിമലർ കാവിൽ പൂരം കാണാൻ... അന്നു നമ്മൾ പോയി രാവിൽ നിലാവിൽ... 🎶")
    
    if x==31:
        
        await event.edit("🎶 കറുകവയൽ കുരുവീ... മുറിവാലൻ കുരുവീ... തളിർ വെറ്റിലയുണ്ടോ... വരദക്ഷിണ വെക്കാൻ... 🎶")
        
    if x==32:
        
        await event.edit("🎶 കുന്നിമണിച്ചെപ്പു തുറന്നെണ്ണി നോക്കും നേരം, പിന്നിൽവന്നു കണ്ണു പൊത്തും കള്ളനെങ്ങു പോയി... 🎶")
        
    if x==33:
        
        await event.edit("Not in a mood to sing. Sorry!")
