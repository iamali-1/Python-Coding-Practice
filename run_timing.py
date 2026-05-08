def trim_float(value: float, before: int, after: int) -> float:
    # Convert to string with enough decimal precision
    s = f"{abs(value):.{after}f}"
    
    # Split into integer and fractional parts
    int_part, frac_part = s.split(".")
    
    # Keep only the requested digits
    int_part = int_part[-before:] if before > 0 else "0"
    frac_part = frac_part[:after] if after > 0 else ""
    
    # Rebuild the number
    result = f"{int_part}.{frac_part}" if after > 0 else int_part
    
    # Restore sign if negative
    if value < 0:
        result = "-" + result
    
    return float(result)

print(trim_float(1234.5678, 2, 3))