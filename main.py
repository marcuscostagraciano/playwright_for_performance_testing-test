import asyncio
from typing import Final, LiteralString

from playwright.async_api import async_playwright

URL_SITE_TRANSPARENCIA: Final[LiteralString] = (
    "https://transparencia.araquari.ifc.edu.br/"
)


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=50)
        page = await browser.new_page()
        await page.goto(URL_SITE_TRANSPARENCIA)
        await browser.close()


asyncio.run(main())
