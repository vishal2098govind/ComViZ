def string_with_arrows(file_text, pos_start, pos_end):
    result = ''

    # Calculate indexes
    idx_start = max(file_text.rfind('\n', 0, pos_start.index), 0)
    idx_end = file_text.rfind('\n', idx_start+1)

    if idx_end < 0:
        idx_end = len(file_text)

    # Generate Each line
    lines = pos_end.line_no - pos_start.line_no + 1
    for line_count in range(lines):

        # Calculate no.of columns in line
        line = file_text[idx_start:idx_end]
        col_start = pos_start.col_no if line_count == 0 else 0
        col_end = pos_end.col_no if line_count == lines-1 else len(line)-1

        # Append arrows to result
        result += line + '\n'
        result += ' ' * col_start + '^' * (col_end-col_start)

        # Re-calculate indexes
        idx_start = idx_end
        idx_end = file_text.find('\n', idx_start+1)
        if idx_end < 0:
            idx_end = len(file_text)
    return result.replace('\t', '')
