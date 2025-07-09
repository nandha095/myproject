from pydantic import BaseModel, EmailStr

class OTPRequest(BaseModel):
    email: EmailStr

class OTPVerify(BaseModel):
    email: EmailStr
    otp: str
    name: str | None = None  # Required only on signup

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


