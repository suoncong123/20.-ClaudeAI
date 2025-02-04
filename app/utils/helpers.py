import re
from typing import List, Dict
from datetime import datetime

def format_timestamp(timestamp: datetime) -> str:
    """Format timestamp thành chuỗi dễ đọc"""
    now = datetime.utcnow()
    diff = now - timestamp
    
    if diff.days == 0:
        if diff.seconds < 60:
            return "Vừa xong"
        if diff.seconds < 3600:
            return f"{diff.seconds // 60} phút trước"
        return f"{diff.seconds // 3600} giờ trước"
    
    if diff.days == 1:
        return "Hôm qua"
        
    if diff.days < 7:
        return f"{diff.days} ngày trước"
        
    return timestamp.strftime("%d/%m/%Y")

def extract_code_blocks(content: str) -> List[Dict[str, str]]:
    """Trích xuất các code block từ nội dung tin nhắn"""
    pattern = r'```(\w+)?\n(.*?)\n```'
    matches = re.finditer(pattern, content, re.DOTALL)
    
    code_blocks = []
    for match in matches:
        language = match.group(1) or 'text'
        code = match.group(2)
        code_blocks.append({
            'language': language,
            'code': code
        })
        
    return code_blocks

def sanitize_filename(filename: str) -> str:
    """Chuyển đổi tên file thành dạng an toàn"""
    # Loại bỏ ký tự đặc biệt
    filename = re.sub(r'[^\w\s-]', '', filename)
    # Thay khoảng trắng bằng dấu gạch ngang
    filename = re.sub(r'\s+', '-', filename)
    return filename.lower()

def truncate_text(text: str, max_length: int = 100) -> str:
    """Cắt ngắn text và thêm dấu ... nếu quá dài"""
    if len(text) <= max_length:
        return text
    return text[:max_length - 3] + '...'