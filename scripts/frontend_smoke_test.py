#!/usr/bin/env python3
"""Public desktop/mobile frontend smoke test. Read only, no logins or form submissions."""
import os
from pathlib import Path
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout

SITE="https://alpencrew.com"
OUT=Path("frontend-audit-artifacts")
OUT.mkdir(exist_ok=True)

def check(page, label):
    errors=[]
    page.on("pageerror", lambda e: errors.append(str(e)[:130]))
    response=page.goto(SITE,wait_until="domcontentloaded",timeout=45000)
    page.wait_for_timeout(3000)
    data=page.evaluate("""() => {
      const pageLinks=Array.from(document.querySelectorAll('a[href]'));
      const imgs=Array.from(document.images);
      const visible=(el)=>{const r=el.getBoundingClientRect();return r.width>0&&r.height>0};
      return {
        title:document.title,
        h1:document.querySelectorAll('h1').length,
        metaDesc:!!document.querySelector('meta[name=description]')?.content?.trim(),
        canonical:!!document.querySelector('link[rel=canonical]')?.href,
        links:pageLinks.length,
        instagramLinks:pageLinks.filter(a=>/instagram\.com/i.test(a.href)).length,
        facebookLinks:pageLinks.filter(a=>/facebook\.com/i.test(a.href)).length,
        whatsappLinks:pageLinks.filter(a=>/(wa\.me|api\.whatsapp\.com)/i.test(a.href)).length,
        ctaLinks:pageLinks.filter(a=>/contact|inquir|enquir|quote|wholesale/i.test((a.innerText||'')+' '+a.href)).length,
        imgCount:imgs.length,
        imgsMissingAlt:imgs.filter(img=>!img.getAttribute('alt')?.trim()).length,
        visibleBrokenImgs:imgs.filter(img=>visible(img)&&img.complete&&img.naturalWidth===0).length,
        horizontalOverflow:document.documentElement.scrollWidth>window.innerWidth+5,
        instagramFeedMarkup:!!document.querySelector('.sbi,.sbi_photo,.instagram-feed,[id^="sb_instagram"]')
      };
    }""")
    page.screenshot(path=str(OUT/f"homepage-{label}.png"),full_page=True,animations="disabled",timeout=45000)
    return response.status if response else "no response",data,len(errors)

with sync_playwright() as p:
    browser=p.chromium.launch(headless=True,args=["--no-sandbox","--disable-dev-shm-usage"])
    configs=[
        ("desktop",{"viewport":{"width":1440,"height":900}}),
        ("mobile",{"viewport":{"width":390,"height":844},"is_mobile":True,"has_touch":True,"device_scale_factor":1})
    ]
    report=["# Alpen Crew — Desktop and Mobile Frontend Smoke Test","","Public homepage only; no WordPress edits, account logins or form submissions.","","| Check | Desktop | Mobile |","|---|---|---|"]
    data={}
    for label,opts in configs:
        context=browser.new_context(**opts,ignore_https_errors=False)
        page=context.new_page()
        try:
            status,measure,errors=check(page,label)
            data[label]={"HTTP":status,**measure,"JavaScript page errors":errors}
        except (PlaywrightTimeout,Exception) as exc:
            data[label]={"Error":type(exc).__name__}
        finally:
            context.close()
    browser.close()
    for key in ["HTTP","title","h1","metaDesc","canonical","links","instagramLinks","facebookLinks","whatsappLinks","ctaLinks","imgCount","imgsMissingAlt","visibleBrokenImgs","horizontalOverflow","instagramFeedMarkup","JavaScript page errors","Error"]:
        if any(key in data[label] for label,_ in configs):
            display=lambda val: str(val).replace("|","/").replace("\n"," ")[:100]
            report.append(f"| {key} | {display(data['desktop'].get(key,'n/a'))} | {display(data['mobile'].get(key,'n/a'))} |")
    report += ["", "Full-page screenshots are saved as workflow artifacts for visual review.","Important: missing alt text includes potentially decorative images; overflows and image reports need visual confirmation."]
    out="\n".join(report)
    print(out)
    summary=os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary,"a",encoding="utf-8") as f:
            f.write(out+"\n")
