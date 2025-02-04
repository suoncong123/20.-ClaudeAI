import re
from typing import Tuple, Optional

def validate_bot_name(name: str) -> Tuple[bool, Optional[str]]:
    """
    Kiểm tra tính hợp lệ của tên bot
    Returns: (is_valid, error_message)
    """
    if not name:
        return False, "Tên bot không được để trống"
    
    if len(name) < 3:
        return False, "Tên bot phải có ít nhất 3 ký tự"
        
    if len(name) > 100:
        return False, "Tên bot không được vượt quá 100 ký tự"
        
    if not re.match(r'^[\w\s-]+$', name):
        return False, "Tên bot chỉ được chứa chữ cái, số, dấu gạch ngang và khoảng trắng"
        
    return True, None

def validate_system_role(role: str) -> Tuple[bool, Optional[str]]:
    """
    Kiểm tra tính hợp lệ của system role
    Returns: (is_valid, error_message)
    """
    if not role:
        return False, "System role không được để trống"
        
    if len(role) < 10:
        return False, "System role quá ngắn"
        
    if len(role) > 4000:
        return False, "System role không được vượt quá 4000 ký tự"
        
    return True, None

def validate_topic_name(name: str) -> Tuple[bool, Optional[str]]:
    """
    Kiểm tra tính hợp lệ của tên topic
    Returns: (is_valid, error_message)
    """
    if not name:
        return False, "Tên topic không được để trống"
    
    if len(name) < 3:
        return False, "Tên topic phải có ít nhất 3 ký tự"
        
    if len(name) > 100:
        return False, "Tên topic không được vượt quá 100 ký tự"
        
    if not re.match(r'^[\w\s-]+$', name):
        return False, "Tên topic chỉ được chứa chữ cái, số, dấu gạch ngang và khoảng trắng"
        
    return True, None

def validate_message(message: str) -> Tuple[bool, Optional[str]]:
    """
    Kiểm tra tính hợp lệ của tin nhắn
    Returns: (is_valid, error_message)
    """
    if not message:
        return False, "Tin nhắn không được để trống"
        
    if len(message) > 4000:
        return False, "Tin nhắn không được vượt quá 4000 ký tự"
        
    return True, None