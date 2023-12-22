def check_magic(filename, magic_bytes):
    """
    checks the provided byte list against the file
    """
    with open(filename, "rb") as fh:
        for bytes_ in magic_bytes:
            data = fh.read(len(bytes_))
            if bytes_ == data:
                return True
            fh.seek(0)
    return False


def is_document_file(filename):
    """
    able to identify most Doc files
    """
    doc_file_magics = (
        b"%PDF", b"\xD0\xCF", b"PK", b"\x14\x00", b"\x1d\x7d",
        b"\xdb\xa5\x2d\x00", b"\x0d\x44\x4f\x43", b"\x50\x4b\x03\x04\x14\x00\x06\x00",
        b"\x7b\x72\x74\x66", b"\x7b\x5c\x72\x74\x66", b"\x7b\x5c\x7b\x5c\x72\x74\x66"
    )
    return check_magic(filename, doc_file_magics)


def is_windows_pe_file(filename):
    """
    identifies both MZ and ZM Windows PE files
    """
    pe_file_magics = (b"\x5a\x4d", b"\x4d\x5a")
    return check_magic(filename, pe_file_magics)


def is_elf_file(filename):
    """
    identifies Linux ELF files
    """
    elf_magics = (b"\x7fELF",)
    return check_magic(filename, elf_magics)
