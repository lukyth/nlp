import json

first = 1
last = 75419

header_list = [
    'x-spamtest-status-extended',
    'x-old-spam-flag',
    'x-spamdetails',
    'x-spamdetect',
    'x-rc-spam',
    'x-activenetwerx-mailscanner-esva-spamscore',
    'x-dspam-signature',
    'x-ktl-spam-status',
    'x-cryst-bbk-mailscanner-spamcheck',
    'x-ufl-spam-status',
    'x-pmx-spam',
    'x-spam-report',
    'x-dspam-confidence',
    'x-internetksc-mailscanner-spamscore',
    'x-barracuda-spam-score',
    'x-pmx-spam-level',
    'x-ms-exchange-organization-antispam-report',
    'x-mxguard-spam-probability',
    'x-report-spam',
    'x-spam_report',
    'x-mailscanner-spamcheck-wiesinger.com',
    'x-dspam-probability',
    'x-dspam-processed',
    'x-kclrealspamscore',
    'x-spam-summary',
    'x-spamtest-method',
    'x-colpos-mailscanner-spamcheck',
    'x-pietru-spamcheck',
    'x-spamtest-version',
    'x-cpanel-mailscanner-spamcheck',
    'x-fhcrc-spam',
    'x-kclspamreport',
    'x-senderbasespam',
    'x-mssl-mailscanner-spamcheck',
    'x-nceas-mercury-mailscanner-spamcheck',
    'x-mailscanner-spamcheck',
    'x-spamtest-group-id',
    'x-old-spam-status',
    'x-perlmx-spam',
    'x-spam-level',
    'x-iss-mailscanner-spamcheck',
    'x-mailscanner-nocs-spamcheck',
    'x-spam-score',
    'x-kazix-mailscanner-spamcheck',
    'x-sgul-mailscanner-spamcheck',
    'x-antispam-id',
    'x-ktl-spam-score',
    'x-no-spam-score',
    'x-spam_score',
    'x-proofpoint-spam-reason',
    'x-spamtest-envelope-from',
    'x-eyou-spamvalue',
    'x-probable-spam',
    'x-spam_score_int',
    'x-nai-spam-rules',
    'x-spam-scored',
    'x-uib-spamflag',
    'x-mms-spam-confidence',
    'x-spam',
    'x-spamgourmet',
    'x-nai-spam-score',
    'x-blackcat-spam-score',
    'x-mobispamstatus',
    'x-brown-mailscanner-spamcheck',
    'x-pm-el-spam-prob',
    'x-uwash-spam',
    'x-spam-scan-date',
    'x-cam-spamdetails',
    'x-spam-dccd-results',
    'x-exchangesecure-antispam',
    'x-dinascanner-spamcheck',
    'x-barracuda-spam-status',
    'x-uea-spam-flag',
    'x-dspam-check',
    'x-iua-mailscanner-spamcheck',
    'x-x-spamdetect',
    'x-s110firewall-mailscanner-spamcheck',
    'x-spam-check-by',
    'x-spamtest-status',
    'x-spamfilter-host',
    'x-spamtest-rate',
    'x-cis-mailscanner-spamcheck',
    'x-nai-spam-level',
    'x-spam-flag',
    'x-uea-spam-score',
    'x-internetksc-mailscanner-spamcheck',
    'x-nai-spam-flag',
    'x-prussianet-mailscanner-spamcheck',
    'x-dspam-factors',
    'x-spamscore',
    'x-unb-spamdetails',
    'x-cce-unipr-ne-mailscanner-spamcheck',
    'x-mailscanner-mluri-spamcheck',
    'x-spam-processed',
    'x-cce-unipr-mailscanner-spamscore',
    'x-old-spam-check-by',
    'x-uib-spamreport',
    'x-ctinetworks-spamcheck',
    'x-spam-tests',
    'x-uqam-spam-filter',
    'x-proofpoint-spam-details',
    'x-spam-checker-version',
    'x-mms-spam-filter-id',
    'x-spam-see',
    'x-spam-prev-subject',
    'x-ironport-anti-spam-filtered',
    'x-s110firewall-mailscanner-spamscore',
    'x-spam-abuse',
    'x-dspam-result',
    'x-spam-rbl-results',
    'x-tmwd-spam-summary',
    'x-nai-spam-threshold',
    'x-ucd-spam-score',
    'x-spam-status',
    'x-spamscan-3',
    'x-spamcatcher-score',
    'x-nai-spam-report',
    'x-kclspamscore',
    'x-dspam-improbability',
    'x-ironport-anti-spam-result',
    'x-coremail-antispam',
    'x-uea-spam-level',
    'x-spam-autolearn',
    'x-spam_bar',
    'x-barracuda-spam-report',
    'x-spamtest-info',
    'x-mxguard-spam-score',
    'x-tud-hrz-mailscanner-spamcheck',
    'x-fb05-mailscanner-spamcheck',
    'x-wp-spam',
    'x-virus-checked',
    'x-barracuda-virus-scanned',
    'x-antivirus-nicochan',
    'x-antivirus-mydomain-message-id',
    'x-antivirus-cmcflex-mail-from',
    'x-ctinetworks-viruscheck',
    'x-antivirus-scanner',
    'x-virus-scanner',
    'x-tpg-antivirus',
    'x-mxguard-virus-info',
    'x-clamantivirus-scanner',
    'x-antivirus',
    'x-copfilter-virus-scanned',
    'x-tkk-virus-scanned',
    'x-proofpoint-virus-version',
    'x-antivirus-arale',
    'x-sohu-antivirus',
    'x-antivirus-cmcflex',
    'x-antivirus-verificado',
    'x-rav-antivirus',
    'x-rc-virus',
    'x-antivirus-acn-mail-from',
    'x-antivirus-acn',
    'x-antivirus-mydomain-mail-from',
    'x-kaspersky-antivirus',
    'x-viruschecked',
    'x-virus-scanned',
    'x-virus-infected',
    'x-antivirus-nicochan-mail-from',
    'x-tud-virus-scanned',
    'x-virus',
    'x-antivirus-acn-message-id',
    'x-mediabeam-virusprotection',
    'x-anti-virus',
    'x-hsu-virusscan',
    'x-cam-antivirus',
    'x-mobivirusstatus',
    'x-unb-virusscanner',
    'x-virus-scan-time',
    'x-gmx-antivirus',
    'x-perlmx-virus-scanned',
    'x-antivirus-status',
    'x-antivirus-mydomain',
    'x-uva-virus-scanned',
    'x-antivirus-code',
    'x-antivirus-arale-mail-from',
    'x-virus-scanned-by',
    'x-virus-status'
]
answer_data = open('../answer')
answer = 0


def print_attr():
    print("@attribute 'header' numeric")
    for attr in header_list:
        print("@attribute '", attr, "' numeric", sep="")
    print("@attribute 'Class' {'spam', 'ham'}")


def print_mail_attr(json_data):
    if 'headers' in json_data:
        print("0, ", end="")
        for header in header_list:
            if header in json_data['headers']:
                print("1, ", end="")
            else:
                print("0, ", end="")
    else:
        print("0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ", end="")


def print_answer(index):
    if index == answer:
        print("'ham'")
    else:
        print("'spam'")


def read_mail(index):
    try:
        json_data = json.load(open('../JSON/inmail.' + str(index) + '.json'))
        print_mail_attr(json_data)
        print_answer(index)
    except:
        pass


def print_mail_data():
    global answer
    for i in range(first, last + 1):
        if i > answer:
            try:
                answer = int(answer_data.readline())
            except:
                answer = 75500
        read_mail(i)


def main():
    print("@relation SpamHam\n")
    print_attr()
    print("\n@data\n")
    print_mail_data()


main()