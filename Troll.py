# ---------------------------------------------------------------------------------
# 鑓塵幗膂蓿f寥寢膃暠瘉甅甃槊槎f碣綮瘋聟碯颱亦尓㍍i:i:i;;:;:: : :
# 澣幗嶌塹傴嫩榛畝皋i袍耘蚌紕欒儼巓襴踟篁f罵f亦尓㍍i:i:i;;:;:: : :
# 漲蔭甃縟諛f麭窶膩I嶮薤篝爰曷樔黎㌢´　　｀ⅷ踟亦尓㍍i:i:i;;:;:: : :
# 蔕漓滿f蕓蟇踴f歙艇艀裲f睚鳫巓襴骸　　　　　贒憊亦尓㍍i:i:i;;:;:: : :
# 榊甃齊爰f懈橈燗殪幢緻I翰儂樔黎夢'”　 　 ,ｨ傾篩縒亦尓㍍i:i:i;;:;:: : :
# 箋聚蜚壊劑薯i暹盥皋袍i耘蚌紕偸′　　　 雫寬I爰曷f亦尓㍍i:i:i;;:;:: : :
# 銕颱麼寰篝螂徑悗f篝嚠篩i縒縡齢　　 　 　 Ⅷ辨f篝I鋗f亦尓㍍i:i:i;;:; : : .
# 碯聟f綴麼辨螢f璟輯駲f迯瓲i軌帶′　　　　　`守I厖孩f奎亦尓㍍i:i:i;;:;:: : : .
# 綮誣撒f曷磔瑩德f幢儂儼巓襴緲′　 　 　 　 　 `守枢i磬廛i亦尓㍍i:i:i;;:;:: : : .
# 慫寫廠徑悗緞f篝嚠篩I縒縡夢'´　　　 　 　 　 　 　 `守峽f徑悗f亦尓㍍i:i:i;;:;:: : : .
# 廛僵I數畝篥I熾龍蚌紕襴緲′　　　　　　　　　　　　　‘守畝皋弊i劍亦尓㍍i:i:i;;:;:: : : .
# 瘧i槲瑩f枢篝磬曷f瓲軌揄′　　　　　　　　　　　　　,gf毯綴徑悗嚠迩忙亦尓㍍i:i:i;;:;::
# 襴罩硼f艇艀裲睚鳫襴鑿緲'　　　　　　　　　　 　 　 奪寔f厦傀揵猯i爾迩忙亦尓㍍i:i:
# 椈棘斐犀耋絎絲絨緲′　　　　　　 　 　 　 　 　 　 　 ”'罨悳萪f蒂渹幇f廏迩忙i亦尓㍍
# 潁樗I瘧德幢i儂巓緲′　　　　　　 　 　 　 　 　 　 r㎡℡〟”'罨椁裂滅楔滄愼愰迩忙亦
# 翦i磅艘溲I搦儼巓登zzz zzz㎜㎜ｧg　 　 緲 g　 　 甯體i爺ゎ｡, ”'罨琥焜毳徭i嵬塰慍絲
# 枢篝磬f曷迯i瓲軌f襴暹 甯幗緲 ,fi'　　 緲',纜｡　　贒i綟碕碚爺ゎ｡ ”'罨皴發傲亂I黹靱
# 緞愾慊嵬嵯欒儼巓襴驫 霤I緲 ,緲　　 ＂,纜穐　　甯絛跨飩i髢馳爺ゎ｡`'等誄I筴碌I畷
# 罩硼I蒻筵硺艇艀i裲睚亀 篳'’,緲　　g亀 Ⅶil齢　　贒罩硼i艇艀裲睚鳫爺靠飭蛸I裘裔
# 椈f棘豢跫跪I衙絎絲絨i爺i㎜iⅣ 　 ,緲i亀 Ⅶ靈,　　甯傅喩I揵揚惹屡絎痙棏敞裔筴敢
# 頬i鞏褂f跫詹雋髢i曷迯瓲軌霤 　 ,緲蔭穐 Ⅶ穐 　 讎椈i棘貅f斐犀耋f絎絲觚f覃黹黍
# 襴蔽戮貲艀舅I肅肄肆槿f蝓Ⅷ 　 緲$慚I穐,疊穐　 甯萪碾f鋗輜靠f誹臧鋩f褂跫詹i雋
# ---------------------------------------------------------------------------------
# 🌐 This project was created https://t.me/I_love_wizzy
# ⚠️ Licensed under the GNU AGPLv3.
# 💢 The owner of this script does not have any responsibility or intellectual property rights in relation to this script.
# ---------------------------------------------------------------------------------
# Name: TrollSpam
# Author: https://t.me/I_love_wizzy
# scope: heroku && hikka
# ---------------------------------------------------------------------------------
__version__ = (1, 0, 0)

import json
import aiohttp
import asyncio
from random import choice
from .. import loader, utils
from telethon.tl.types import Message

@loader.tds
class KomarutrollMod(loader.Module):
    """Module for insults, make the interlocuter depressed."""

    strings = {
        "name": "KomaruTroll",
        "error_key": "<b><i>Error: Key 'TrollText' not found.</i></b>",
        "error_decoding": "<b><i>Error: The JSON could not be decoded.</i></b>",
        "error_uploading_data": "<b><i>Error loading data</i></b>",
        "error_valid_args": "<b><i>Please enter valid arguments!</i></b>",
        "launched": "<b><i>KomaruTroll launched!</i></b>\n\n<b><i>Use <code>{prefix}komaruoff</code> to stop the attack.</i></b>",
        "stopped": "<b><i>KomaruTroll has stopped.</i></b>",
    }

    strings_ru = {
        "error_key": "<b><i>Error: ключ 'TrollText' не найден.</i></b>",
        "error_decoding": "<b><i>Error: не удалось декодировать JSON.</i></b>",
        "error_uploading_data": "<b><i>Ошибка при загрузке данных</i></b>",
        "error_valid_args": "<b><i>Введите корректные аргументы!</i></b>",
        "launched": "<b><i>KomaruTroll запущен!</i></b>\n\n<b><i>Используйте <code>{prefix}komaruoff</code>, чтобы остановить атаку.</i></b>",
        "stopped": "<b><i>KomaruTroll остановлен.</i></b>",
    }

    strings_uz = {
        "error_key": "<b><i>Error: 'TrollText' калити топилмади.</i></b>",
        "error_decoding": "<b><i>Error: JSON декодлаш муваффақиятли амалга ошмади.</i></b>",
        "error_uploading_data": "<b><i>Маълумотлар юклаб олинмади</i></b>",
        "error_valid_args": "<b><i>Iltimos, to'g'ri dalillarni kiriting!</i></b>",
        "launched": "<b><i>KomaruTroll ishga tushirildi!</i></b>\n\n<b><i>Hujumni toʻxtatish uchun <code>{prefix}komaruoff</code> dan foydalaning.</i></b>",
        "stopped": "<b><i>KomaruTroll to'xtadi.</i></b>",
    }

    strings_de = {
        "error_key": "<b><i>Error: Der Schlüssel 'TrollText' wurde nicht gefunden.</i></b>",
        "error_decoding": "<b><i>Error: JSON konnte nicht decodiert werden.</i></b>",
        "error_uploading_data": "<b><i>Fehler beim Hochladen der Daten</i></b>",
        "error_valid_args": "<b><i>Bitte geben Sie gültige Argumente ein!</i></b>",
        "launched": "<b><i>KomaruTroll gestartet!</i></b>\n\n<b><i>Verwenden Sie <code>{prefix}komaruoff</code>, um den Angriff zu stoppen.</i></b>",
        "stopped": "<b><i>KomaruTroll hat angehalten.</i></b>",
    }

    strings_es = {
        "error_key": "<b><i>Error: No se encontró la clave 'TrollText'.</i></b>",
        "error_decoding": "<b><i>Error: No se pudo decodificar JSON.</i></b>",
        "error_uploading_data": "<b><i>Error al cargar los datos</i></b>",
        "error_valid_args": "<b><i>¡Por favor ingrese argumentos válidos!</i></b>",
        "launched": "<b><i>¡KomaruTroll lanzado!</i></b>\n\n<b><i>Utiliza <code>{prefix}komaruoff</code> para detener el ataque.</i></b>",
        "stopped": "<b><i>KomaruTroll se ha detenido.</i></b>",
    }

    async def client_ready(self, client, db):
        self.client = client
        self.db = db
        self.is_active = False

    @loader.command(
        ru_doc="Оскорбите вашего собеседника.",
        uz_doc="Suhbatdoshingizni insult qiling.",
        de_doc="Beleidigen Sie Ihren Gesprächspartner.",
        es_doc="Insulta a tu interlocutor.",
    )
    async def komarutroll(self, message):
        """Insult your interlocutor"""
        url = "https://raw.githubusercontent.com/komarulolll/herokutrollsr/main/TrollText.json"
        
        if not message.is_reply:
            await utils.answer(message, "<b><i>Reply to a message!</i></b>")
            return
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    response_text = await response.text()
                    try:
                        data = json.loads(response_text)
                        if "TrollText" in data and isinstance(data["TrollText"], list) and data["TrollText"]:
                            text = choice(data["TrollText"])
                            
                            replied_msg = await message.get_reply_message()
                            words = text.split()
                            
                            for word in words:
                                if not self.is_active:
                                    break
                                await self.client.send_message(
                                    message.chat_id,
                                    word,
                                    reply_to=replied_msg.id
                                )
                                await asyncio.sleep(0.1)
                                
                        else:
                            await utils.answer(message, self.strings("error_key"))
                    except json.JSONDecodeError:
                        await utils.answer(message, self.strings("error_decoding"))
                else:
                    await utils.answer(message, f"{self.strings('error_uploading_data')}: {response.status}")

    @loader.command(
        ru_doc="[time] [text] - Заспамте оскорблениями вашего собеседника",
        uz_doc="[time] [text] - Suhbatdoshingizni haqorat bilan spam qiling",
        de_doc="[time] [text] - Spammen Sie Ihren Gesprächspartner mit Beleidigungen zu",
        es_doc="[time] [text] - Spamea a tu interlocutor con insultos",
    )
    async def komaruspam(self, message: Message):
        """[time] [text] - Spam your interlocutor with insults"""
        url = "https://raw.githubusercontent.com/komarulolll/herokutrollsr/main/TrollText.json"
        args = utils.get_args(message)

        if not message.is_reply:
            await utils.answer(message, "<b><i>Reply to a message!</i></b>")
            return

        if not args:
            await utils.answer(message, self.strings("error_valid_args"))
            return
        else:
            self.is_active = True

        try:
            time = float(args[0])
            text = ' '.join(args[1:]) + " " if len(args) > 1 else ""
        except ValueError:
            await utils.answer(message, self.strings("error_valid_args"))
            return

        await utils.answer(message, self.strings("launched").format(prefix=self.get_prefix()))
        
        replied_msg = await message.get_reply_message()
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    response_text = await response.text()
                    
                    try:
                        data = json.loads(response_text)
                        if "TrollText" in data and isinstance(data["TrollText"], list) and data["TrollText"]:
                            while self.is_active:
                                bull_text = choice(data["TrollText"])
                                words = bull_text.split()
                                for word in words:
                                    if not self.is_active:
                                        break
                                    await message.client.send_message(
                                        message.chat_id,
                                        word,
                                        reply_to=replied_msg.id
                                    )
                                    await asyncio.sleep(0.1)
                                await asyncio.sleep(time)
                            return
                        else:
                            return await utils.answer(message, self.strings("error_key"))
                    except json.JSONDecodeError:
                        return await utils.answer(message, self.strings("error_decoding"))
                else:
                    return await utils.answer(message, f"{self.strings('error_uploading_data')}: {response.status}")

    @loader.command(
        ru_doc="Остановить оскорбления",
        uz_doc="Haqoratlarni to'xtating",
        de_doc="Hört auf mit den Beleidigungen",
        es_doc="basta de insultos",
    )
    async def komaruoff(self, message: Message):
        """Stop the insults"""
        self.is_active = False
        await utils.answer(message, self.strings("stopped"))
        return
