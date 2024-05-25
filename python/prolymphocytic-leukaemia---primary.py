# Sara Muller, Samantha L Hider, Karim Raza, Rebecca J Stack, Richard A Hayward, Christian D Mallen, 2024.

import sys, csv, re

codes = [{"code":"B620100","system":"readv2"},{"code":"B614400","system":"readv2"},{"code":"B616400","system":"readv2"},{"code":"B64y400","system":"readv2"},{"code":"B61z200","system":"readv2"},{"code":"B625200","system":"readv2"},{"code":"B616z00","system":"readv2"},{"code":"B620500","system":"readv2"},{"code":"B62y400","system":"readv2"},{"code":"B602200","system":"readv2"},{"code":"B600100","system":"readv2"},{"code":"B62y200","system":"readv2"},{"code":"B620800","system":"readv2"},{"code":"B61z400","system":"readv2"},{"code":"B616700","system":"readv2"},{"code":"B614200","system":"readv2"},{"code":"B623100","system":"readv2"},{"code":"B625800","system":"readv2"},{"code":"B621500","system":"readv2"},{"code":"B620200","system":"readv2"},{"code":"B62y100","system":"readv2"},{"code":"B6z0.00","system":"readv2"},{"code":"B614800","system":"readv2"},{"code":"B61z800","system":"readv2"},{"code":"B600300","system":"readv2"},{"code":"B615200","system":"readv2"},{"code":"B624300","system":"readv2"},{"code":"B601200","system":"readv2"},{"code":"B616.00","system":"readv2"},{"code":"B623300","system":"readv2"},{"code":"B64y100","system":"readv2"},{"code":"B61z500","system":"readv2"},{"code":"B620300","system":"readv2"},{"code":"B616000","system":"readv2"},{"code":"B601500","system":"readv2"},{"code":"B62z100","system":"readv2"},{"code":"B621300","system":"readv2"},{"code":"B601300","system":"readv2"},{"code":"B62y500","system":"readv2"},{"code":"B601100","system":"readv2"},{"code":"B615100","system":"readv2"},{"code":"B641011","system":"readv2"},{"code":"B62y800","system":"readv2"},{"code":"B62z400","system":"readv2"},{"code":"B621800","system":"readv2"},{"code":"B641000","system":"readv2"},{"code":"B602300","system":"readv2"},{"code":"B61z100","system":"readv2"},{"code":"B602500","system":"readv2"},{"code":"B614300","system":"readv2"},{"code":"B601800","system":"readv2"},{"code":"B62y300","system":"readv2"},{"code":"B616800","system":"readv2"},{"code":"B602100","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('leukaemia-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["prolymphocytic-leukaemia---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["prolymphocytic-leukaemia---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["prolymphocytic-leukaemia---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
