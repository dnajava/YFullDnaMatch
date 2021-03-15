# from difflib import SequenceMatcher
from File import File

def show(li: list):
    print('Snps\tDiff\tDist\t\tYF\t\t\tHaplo\t\tOldest')

    print('YFull STR match list:')
    for x in li:
        print(x[0], '\t', x[1], '\t', x[2], '\t', x[3], '\t', x[5], '\t', x[4])


if __name__ == '__main__':
    tunnukset = ['AAA', 'BBB']
    lim_str, lim_snp = [[], []]
    same_snp, same_str = 0, 0

    lim_snp.append(File.read_snp((tunnukset[0]) + '_SNP-match.csv'))
    lim_str.append(File.read_snp((tunnukset[0]) + '_STR-match.csv'))

    lim_snp.append(File.read_snp((tunnukset[1]) + '_SNP-match.csv'))
    lim_str.append(File.read_snp((tunnukset[1]) + '_STR-match.csv'))

    print('Kit', tunnukset[0], ' SNP-mätsejä', len(lim_snp[0]), 'ja STR-mätsejä', len(lim_str[0]))
    print('Kit', tunnukset[1], ' SNP-mätsejä', len(lim_snp[1]), 'ja STR-mätsejä', len(lim_str[1]))

    exit(0)

    for a in lim_snp:
        for b in lim_snp:
            if len(a[3]) == len(b[3]):
                sameletter = True
                for i in range(0, len(a[3])):
                    if a[3][i] != b[3][i]:
                        sameletter = False
                if sameletter:
                    same_snp += 1

    for a in lim_str:
        for b in lim_str:
            if len(a[3]) == len(b[3]):
                sameletter = True
                for i in range(0, len(a[3])):
                    if a[3][i] != b[3][i]:
                        sameletter = False
                if sameletter:
                    same_str += 1

    for i in range(0, len(tunnukset)-1):
        print(tunnukset[i], 'SNP-mätsejä', len(lim_snp[i]), 'kpl ja STR-mätsejä', len(lim_str[i]), 'kpl.')
        print('Samoja SNP-mätsejä', same_snp, 'kpl ja samoja STR-mätsejä', same_str, 'kpl.')
