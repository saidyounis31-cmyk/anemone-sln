import os
from typing import Optional
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    title="ANEMONE SLN - Universal Medical & Clinical AI Agent",
    description="Established 2020 | Clinical AI Engine Backend",
    version="1.0.0"
)

# تفعيل CORS للربط مع واجهة Vercel الأمامية
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# بنية بيانات طلب التحليل السريري
class ClinicalRequest(BaseModel):
    user_id: str
    user_name: str
    badge_type: str  # 'Dietitian', 'Herbalist', 'Nurse', 'Doctor', 'Naturopath', 'Student'
    subscription_tier: str  # 'free', 'student', 'doctor'
    case_description: str

@app.get("/")
def health_check():
    return {
        "platform": "ANEMONE SLN",
        "since": 2020,
        "status": "Operational",
        "engine": "FastAPI 24/7 Production Engine"
    }

@app.post("/api/clinical/analyze")
async def analyze_clinical_case(data: ClinicalRequest):
    is_paid_tier = data.subscription_tier.lower() in ["student", "doctor"]
    
    specialty_focus = {
        "Dietitian": "التركيز السريري: الماكرونات، الميكرونات، السعرات، والتداخلات الغذائية (דיאטנית קלינית)",
        "Herbalist": "التركيز السريري: المعايرة الكيميائية، نسب المستخلصات (1:1 / 1:5)، والمواد الفعالة",
        "Nurse": "التركيز السريري: العلامات الحيوية، أمان الإدارة العلاجية، والبروتوكولات التمريضية",
        "Doctor": "التركيز السريري: التشخيص الفارقي المزدوج، الاستجابة البيوكيميائية، وإدارة المخاطر",
        "Student": "التركيز الأكاديمي: الشرح المفصل، المراجع العلمية، والخرائط الذهنية"
    }.get(data.badge_type, "التحليل الطبي والتكافلي الشامل")

    response_payload = {
        "meta": {
            "platform": "ANEMONE SLN (SINCE 2020)",
            "prepared_for": f"{data.user_name}",
            "badge_applied": data.badge_type,
            "specialty_focus": specialty_focus
        },
        "open_content": {
            "pathology_analysis": f"تحليل الآلية المرضية للحالة: {data.case_description[:100]}...",
            "candidate_botanicals": ["الكركمين المعاير", "مستخلص الجلايسيريزين", "زيت النعناع المغلف"]
        },
        "gated_content": {
            "exact_dosages": "350 mg مرتين يومياً قبل الوجبة بـ 30 دقيقة" if is_paid_tier else "🔒 [مغلق: يتطلب اشتراك فتح الجرعات الموزونة]",
            "cyp450_interactions": "تداخل نشط على إنزيم CYP3A4 في الكبد" if is_paid_tier else "🔒 [مغلق: مخصص للمشتركين لتفادي التداخلات الدوائية]",
            "savant_3d_view": "ENABLED_MODEL_ID_8821" if is_paid_tier else "🔒 [معايرة نموذج د. ميرفي 3D مقتصرة على الباقات المدفوعة]"
        }
    }
    
    return response_payload

