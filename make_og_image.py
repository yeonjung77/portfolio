"""
OG 썸네일 이미지 생성 (1200x630)
- 좌측: 프로필 사진
- 우측: 이름, 태그라인, 이력 요약
"""
from PIL import Image, ImageDraw, ImageFont
import os

# 색상
BG = (255, 255, 255)
PRIMARY = (17, 17, 17)
ACCENT = (176, 141, 106)
TEXT = (51, 51, 51)
TEXT_LIGHT = (119, 119, 119)
BORDER = (229, 229, 229)

W, H = 1200, 630

# 캔버스
img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

# 좌측 사이드바 배경
SIDEBAR_W = 480
draw.rectangle([0, 0, SIDEBAR_W, H], fill=(248, 248, 247))

# 프로필 사진 (좌측 중앙)
profile = Image.open("assets/img/profile.jpg")
# 정방형으로 크롭 (얼굴 중심)
pw, ph = profile.size
side = min(pw, ph)
left = (pw - side) // 2
top = int(ph * 0.05)  # 얼굴이 위쪽이라 위에서 5% 지점부터
if top + side > ph:
    top = ph - side
profile_cropped = profile.crop((left, top, left + side, top + side))
profile_resized = profile_cropped.resize((320, 320), Image.LANCZOS)

# 원형 마스크
mask = Image.new("L", (320, 320), 0)
mask_draw = ImageDraw.Draw(mask)
mask_draw.ellipse((0, 0, 320, 320), fill=255)

# 사진 붙이기
photo_x = (SIDEBAR_W - 320) // 2
photo_y = (H - 320) // 2
img.paste(profile_resized, (photo_x, photo_y), mask)

# 폰트 로드 (시스템 폰트)
def load_font(size, bold=False):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ]
    for path in candidates:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()

font_label = load_font(20, bold=True)
font_title = load_font(56, bold=True)
font_tagline = load_font(22)
font_body = load_font(18)
font_small = load_font(16, bold=True)

# 우측 텍스트 영역
TEXT_X = SIDEBAR_W + 60
y = 130

# Label
draw.text((TEXT_X, y), "FASHION + AI", font=font_label, fill=ACCENT)
y += 40

# Name
draw.text((TEXT_X, y), "Yeonjung Won", font=font_title, fill=PRIMARY)
y += 80

# Tagline
draw.text((TEXT_X, y), "Bridging Fashion Expertise with AI", font=font_tagline, fill=TEXT_LIGHT)
y += 32
draw.text((TEXT_X, y), "to Build Practical Solutions", font=font_tagline, fill=TEXT_LIGHT)
y += 60

# 구분선
draw.rectangle([TEXT_X, y, TEXT_X + 60, y + 3], fill=ACCENT)
y += 30

# 이력 요약 (작은 글씨)
items = [
    "Kakao Tech Bootcamp - AI Development",
    "M.S. Yonsei University - Fashion Consumer Psychology",
    "ex-SF Lab Inc. - Fashion Data & Service Planning",
]
for item in items:
    draw.text((TEXT_X, y), item, font=font_body, fill=TEXT)
    y += 30

# 저장
img.save("assets/img/og_thumbnail.png", "PNG")
print("OG 썸네일 생성 완료: assets/img/og_thumbnail.png")
print(f"크기: {W}x{H}")
