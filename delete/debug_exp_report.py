
from math import ceil
from typing import Iterable, List, Optional, Tuple

def format_hms(total_seconds: float) -> str:
    s = int(round(total_seconds))
    h, rem = divmod(s, 3600)
    m, s = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"

def _format_thousands(n: int) -> str:
    return f"{n:,}".replace(",", ".")

def _validate_inputs(
    total_exp: int,
    exp_per_cycle: int,
    min_sec_per_cycle: int,
    max_sec_per_cycle: int,
    detail_checkpoints: Optional[Iterable[int]],
) -> None:
    if not isinstance(total_exp, int) or total_exp <= 0:
        raise ValueError("total_exp debe ser int > 0")
    if not isinstance(exp_per_cycle, int) or exp_per_cycle <= 0:
        raise ValueError("exp_per_cycle debe ser int > 0")
    if not isinstance(min_sec_per_cycle, int) or min_sec_per_cycle <= 0:
        raise ValueError("min_sec_per_cycle debe ser int > 0")
    if not isinstance(max_sec_per_cycle, int) or max_sec_per_cycle <= 0:
        raise ValueError("max_sec_per_cycle debe ser int > 0")
    if min_sec_per_cycle > max_sec_per_cycle:
        raise ValueError("min_sec_per_cycle no puede ser mayor que max_sec_per_cycle")
    if detail_checkpoints is not None:
        for cp in detail_checkpoints:
            if not isinstance(cp, int) or cp <= 0:
                raise ValueError("Todos los checkpoints deben ser int > 0")

def _compute_plan(
    total_exp: int,
    exp_per_cycle: int,
    min_sec_per_cycle: int,
    max_sec_per_cycle: int,
    detail_checkpoints: Optional[Iterable[int]] = None,
) -> str:
    cycles_needed = ceil(total_exp / exp_per_cycle)
    total_min_seconds = cycles_needed * min_sec_per_cycle
    total_max_seconds = cycles_needed * max_sec_per_cycle
    lines: List[str] = []
    lines.append("=== Debug EXP Report ===")
    lines.append(f"total_exp: {_format_thousands(total_exp)}")
    lines.append(f"exp_per_cycle: {exp_per_cycle}")
    lines.append(f"Ciclos necesarios (ceil): {cycles_needed}")
    lines.append("")
    lines.append(f"min_sec_per_cycle: {min_sec_per_cycle}")
    lines.append(f"Tiempo total mínimo: {format_hms(total_min_seconds)}")
    lines.append("")
    lines.append(f"max_sec_per_cycle: {max_sec_per_cycle}")
    lines.append(f"Tiempo total máximo: {format_hms(total_max_seconds)}")
    if detail_checkpoints:
        seen = set()
        checkpoints_unique: List[int] = []
        for cp in detail_checkpoints:
            if cp not in seen:
                seen.add(cp)
                checkpoints_unique.append(cp)
        header_cols: Tuple[str, str, str, str] = (
            "Checkpoint",
            "Ciclos hasta aquí",
            "Tiempo mínimo",
            "Tiempo máximo",
        )
        lines.append("")
        w_checkpoint = 13
        w_cycles = 20
        w_time = 16
        lines.append(
            f"{header_cols[0]:>{w_checkpoint}}"
            f"{header_cols[1]:>{w_cycles}}"
            f"{header_cols[2]:>{w_time}}"
            f"{header_cols[3]:>{w_time}}"
        )
        lines.append("-" * (w_checkpoint + w_cycles + w_time * 2))
        for cp in checkpoints_unique:
            cyc = ceil(cp / exp_per_cycle)
            tmin = cyc * min_sec_per_cycle
            tmax = cyc * max_sec_per_cycle
            lines.append(
                f"{_format_thousands(cp):>{w_checkpoint}}"
                f"{cyc:>{w_cycles}d}"
                f"{format_hms(tmin):>{w_time}}"
                f"{format_hms(tmax):>{w_time}}"
            )
    return "\n".join(lines)

def debug_exp_report(
    total_exp: int,
    exp_per_cycle: int,
    min_sec_per_cycle: int,
    max_sec_per_cycle: int,
    detail_checkpoints: Optional[Iterable[int]] = None,
) -> None:
    _validate_inputs(
        total_exp,
        exp_per_cycle,
        min_sec_per_cycle,
        max_sec_per_cycle,
        detail_checkpoints,
    )
    output = _compute_plan(
        total_exp,
        exp_per_cycle,
        min_sec_per_cycle,
        max_sec_per_cycle,
        detail_checkpoints,
    )
    print(output)

debug_exp_report(57000,60,45,60,detail_checkpoints=[1000,2000,3125,4125,5125,6250,7250,8375,9375,10375])
debug_exp_report(28875,60,45,60,[15375,13500])