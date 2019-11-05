import sys

vcard = """BEGIN:VCARD
VERSION:2.1
N:{0};{1};;;
FN:{1} {0}
TEL;CELL:{2}
END:VCAR
"""

def print_help():
    print('Transform Motorola RAZR contact to Samsung S3 vCard format')
    print('Usage:')
    print('transform.py <csv_filename> <vcard_filename>')

def export_to_vcf(csv_filename, vcf_filename):
    with open(csv_filename, 'rt') as f, open(vcf_filename, 'wt') as fo:
        for line in f:
            line = line.strip()
            print(line)
            _, _, full_name, _, tel_no, *_ = line.split(';')
            
            full_name_splitted = full_name.split(' ')
            if len(full_name_splitted) > 1:
                name, surname, *rest = full_name_splitted
            else:
                name, surname = full_name, ''

            s = vcard.format(surname, name, tel_no)

            fo.write(s)


def main():
    if len(sys.argv) != 3:
        print_help()
    else:
        export_to_vcf(sys.argv[1], sys.argv[2])


if __name__ == '__main__':
    main()