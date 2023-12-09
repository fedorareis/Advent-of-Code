from functools import reduce


ex = {
    "11A": ("11B", "XXX"),
    "11B": ("XXX", "11Z"),
    "11Z": ("11B", "XXX"),
    "22A": ("22B", "XXX"),
    "22B": ("22C", "22C"),
    "22C": ("22Z", "22Z"),
    "22Z": ("22B", "22B"),
    "XXX": ("XXX", "XXX"),
}
exNav = "LR"
exStart = ["11A", "22A"]

input = {
    "LRL": ("MCG", "TRC"),
    "TNJ": ("LMV", "PMP"),
    "GQK": ("MGD", "DBP"),
    "KVK": ("LHC", "NMM"),
    "PQX": ("SLC", "LSD"),
    "GRR": ("XCR", "BJT"),
    "RBF": ("VDM", "BFG"),
    "TKN": ("VDH", "HGQ"),
    "MMJ": ("LTR", "CNQ"),
    "CCX": ("FJJ", "FKD"),
    "VHD": ("JFQ", "DDH"),
    "NRL": ("CTM", "XTJ"),
    "SNH": ("QDH", "PSQ"),
    "JTM": ("VFH", "QBR"),
    "BJT": ("GJL", "JXD"),
    "LBJ": ("JFQ", "DDH"),
    "FPN": ("PBT", "SJR"),
    "CGR": ("NJC", "CNF"),
    "RCM": ("GTQ", "BBT"),
    "BQQ": ("FNS", "KPL"),
    "NSF": ("SLD", "SJV"),
    "QFQ": ("XNX", "GHT"),
    "QCZ": ("JPG", "NLJ"),
    "RJD": ("QDT", "NSG"),
    "CNK": ("SKK", "NFL"),
    "CBR": ("QDT", "NSG"),
    "QMV": ("HXG", "FHS"),
    "DNL": ("XLX", "RDT"),
    "XRS": ("DHT", "RDP"),
    "GHV": ("FHS", "HXG"),
    "MJM": ("GQB", "XCC"),
    "GQC": ("NKG", "NSF"),
    "RKH": ("KVG", "JCQ"),
    "DKT": ("LTN", "LTN"),
    "THR": ("PHF", "VKN"),
    "BQV": ("BTS", "SCG"),
    "BJJ": ("GQC", "QRR"),
    "CQL": ("LHK", "BCD"),
    "LXX": ("LCX", "FJV"),
    "NSG": ("VSX", "DFN"),
    "LSD": ("JRL", "KXC"),
    "QKB": ("NLJ", "JPG"),
    "HSK": ("CFN", "NTM"),
    "BLL": ("JJQ", "MSN"),
    "SQD": ("BLK", "LBK"),
    "KVP": ("DBB", "RHN"),
    "MLJ": ("QQR", "HDH"),
    "QVB": ("GMN", "TDP"),
    "HJB": ("GPG", "XDT"),
    "NBX": ("NVT", "SNB"),
    "CLL": ("PLG", "LHS"),
    "AAA": ("JXS", "MFQ"),
    "CHN": ("RNL", "FHV"),
    "JHT": ("JQF", "JQX"),
    "KSB": ("VDL", "VBD"),
    "HBT": ("CKB", "CCX"),
    "JXH": ("MQH", "PRD"),
    "DBB": ("XHL", "CHN"),
    "PBD": ("RDB", "VHH"),
    "SDV": ("VMG", "NTV"),
    "BJS": ("NNG", "RQH"),
    "SLM": ("BRB", "FLG"),
    "VDH": ("QPG", "GKG"),
    "KNS": ("VQX", "HFR"),
    "HBF": ("RQC", "MXC"),
    "JSF": ("KPL", "FNS"),
    "HLS": ("TJQ", "TKM"),
    "TRV": ("BVN", "GKF"),
    "NLJ": ("GBH", "JCT"),
    "SVM": ("DKT", "XLG"),
    "THK": ("NTM", "CFN"),
    "MDK": ("DNL", "VXV"),
    "MHV": ("DQQ", "MQX"),
    "CNF": ("QQH", "SLN"),
    "XJK": ("VFH", "QBR"),
    "FNT": ("HXR", "HXR"),
    "KCT": ("CPX", "FXC"),
    "BDB": ("NMP", "JGG"),
    "LRZ": ("JXC", "TNJ"),
    "JBQ": ("NDL", "KSJ"),
    "LJQ": ("GHT", "XNX"),
    "HKD": ("HFH", "VHJ"),
    "VDM": ("GTD", "HRP"),
    "QQH": ("THC", "THR"),
    "PRD": ("KFR", "TJK"),
    "KKH": ("VTJ", "LSR"),
    "LQS": ("SJQ", "RHD"),
    "RLF": ("LCR", "SGG"),
    "JHK": ("PDJ", "TRV"),
    "QHG": ("VMS", "PKS"),
    "JRL": ("GVJ", "SKL"),
    "XDV": ("PJL", "JRN"),
    "TSV": ("KCR", "QJP"),
    "JSN": ("QFQ", "LJQ"),
    "RLA": ("JSN", "JVD"),
    "KPD": ("RDK", "NSS"),
    "HXP": ("RQT", "QTS"),
    "DDB": ("SFH", "RHV"),
    "JGG": ("BJG", "JTS"),
    "VBD": ("SGD", "FRJ"),
    "HRP": ("RJD", "CBR"),
    "RRT": ("MLJ", "MLJ"),
    "NVD": ("KHM", "RBF"),
    "TNK": ("QSX", "KVD"),
    "NST": ("CDL", "VGL"),
    "FLF": ("SNF", "KRN"),
    "LHS": ("BSD", "DTD"),
    "NCV": ("KSB", "PTG"),
    "FMX": ("QKX", "XFP"),
    "KMB": ("FDM", "BSX"),
    "CRH": ("CVV", "DDS"),
    "VGL": ("JLS", "CPK"),
    "DBF": ("KGB", "PXQ"),
    "RNM": ("HTP", "LVL"),
    "HKC": ("XML", "RTK"),
    "JLC": ("TKN", "VSV"),
    "FLB": ("NNG", "RQH"),
    "QKH": ("GQM", "LSB"),
    "DTD": ("FTJ", "HCK"),
    "BXS": ("HKD", "FDK"),
    "TKV": ("RHN", "DBB"),
    "QBJ": ("KNS", "DXQ"),
    "LBS": ("BHT", "SFM"),
    "VMS": ("CTJ", "DDC"),
    "FQJ": ("FVQ", "GKR"),
    "RQC": ("LRF", "HCM"),
    "SSG": ("GQK", "HDV"),
    "KPL": ("GQS", "MDK"),
    "GJN": ("PNN", "CPB"),
    "LHK": ("QPD", "GSV"),
    "KFR": ("KPD", "DTV"),
    "QXC": ("QVM", "BHJ"),
    "XRH": ("PKM", "FPN"),
    "CKL": ("BBT", "GTQ"),
    "FPK": ("CRV", "MGR"),
    "LTK": ("LVT", "HXF"),
    "BLK": ("BRT", "BQN"),
    "BSX": ("XMS", "XJN"),
    "MMR": ("JCG", "HHX"),
    "DVM": ("LHK", "BCD"),
    "RCJ": ("BDB", "CFK"),
    "QLN": ("DDB", "LDQ"),
    "GKF": ("QLV", "FNP"),
    "BXQ": ("NKT", "FFN"),
    "HCM": ("FPK", "KQB"),
    "HKG": ("GQK", "HDV"),
    "FNS": ("GQS", "MDK"),
    "CTJ": ("NST", "HDJ"),
    "QQS": ("GQB", "XCC"),
    "ZZZ": ("MFQ", "JXS"),
    "MGK": ("CRH", "BRV"),
    "LCR": ("FRD", "KMK"),
    "BKD": ("BNR", "BKM"),
    "LDB": ("KLM", "SCC"),
    "PLS": ("PBL", "CRG"),
    "FQR": ("PNR", "NCV"),
    "TNL": ("CDT", "MKC"),
    "KVH": ("FJQ", "SHJ"),
    "KPT": ("KGB", "PXQ"),
    "GQM": ("BXQ", "VLP"),
    "FDR": ("GLC", "KGF"),
    "DDC": ("NST", "HDJ"),
    "MTJ": ("TMT", "TMB"),
    "PBJ": ("LTK", "VFB"),
    "JXS": ("SBL", "CQB"),
    "XML": ("BMK", "QBL"),
    "XSK": ("KSN", "KSN"),
    "TKM": ("TKQ", "NTX"),
    "XFP": ("HBX", "RMX"),
    "DXQ": ("VQX", "HFR"),
    "KRN": ("CNK", "JDM"),
    "TJQ": ("TKQ", "NTX"),
    "VQX": ("LBJ", "VHD"),
    "TGX": ("HLK", "LDJ"),
    "MCX": ("GDH", "BNS"),
    "DKM": ("TVC", "LPB"),
    "VXD": ("GCF", "SVD"),
    "FGB": ("BKM", "BNR"),
    "VNN": ("VCS", "BSR"),
    "FXX": ("LHC", "NMM"),
    "JKR": ("TQN", "GXV"),
    "FRJ": ("TDK", "PKQ"),
    "MMQ": ("SCC", "KLM"),
    "XGL": ("MSN", "JJQ"),
    "GTQ": ("DMV", "LLK"),
    "KML": ("MCX", "CTT"),
    "LBH": ("LSR", "VTJ"),
    "BDS": ("XJK", "JTM"),
    "FVH": ("TSV", "HHC"),
    "KXN": ("LRL", "QKK"),
    "HND": ("HNQ", "FSG"),
    "JQS": ("QLL", "RKH"),
    "CKD": ("TBT", "HBT"),
    "PXP": ("NXC", "TTK"),
    "VHP": ("QJC", "QKH"),
    "KQL": ("BQV", "RJR"),
    "FSG": ("JBH", "GPH"),
    "BVN": ("QLV", "FNP"),
    "HNV": ("XFH", "BKL"),
    "CNJ": ("MNT", "DCG"),
    "VSV": ("HGQ", "VDH"),
    "PXB": ("RRT", "RRT"),
    "FNK": ("TKC", "LTM"),
    "VTX": ("LDJ", "HLK"),
    "KKG": ("QDL", "SNT"),
    "CTT": ("GDH", "BNS"),
    "FJJ": ("FNT", "FNT"),
    "JCS": ("DDB", "LDQ"),
    "GDH": ("TPG", "DND"),
    "FMF": ("XHB", "BNH"),
    "QLL": ("JCQ", "KVG"),
    "NJK": ("RDB", "VHH"),
    "LHC": ("QDS", "SXP"),
    "QHS": ("KQL", "SXQ"),
    "BJQ": ("BXB", "HQT"),
    "GJL": ("BTX", "GJC"),
    "BNR": ("NJK", "PBD"),
    "NFL": ("NSC", "FTL"),
    "SKK": ("FTL", "NSC"),
    "MQN": ("FMF", "KPC"),
    "XHB": ("DCS", "SQD"),
    "MDT": ("TDP", "GMN"),
    "XBL": ("TMT", "TMB"),
    "HFH": ("XDV", "DMD"),
    "BSR": ("VTX", "TGX"),
    "LDH": ("BJQ", "XJJ"),
    "GXX": ("KKL", "RCJ"),
    "PQZ": ("HDH", "QQR"),
    "CXH": ("VXD", "SGC"),
    "HPB": ("VHR", "FNQ"),
    "LLF": ("QVM", "BHJ"),
    "VQQ": ("FQD", "MQN"),
    "GSV": ("NDT", "SLM"),
    "GLR": ("HVD", "DMF"),
    "SLC": ("JRL", "KXC"),
    "RHV": ("HBC", "TFR"),
    "PVX": ("PLS", "SJS"),
    "LLK": ("BDC", "PNK"),
    "SLL": ("FJQ", "SHJ"),
    "LKT": ("VPF", "SSC"),
    "MXC": ("LRF", "HCM"),
    "FTL": ("QSR", "SVH"),
    "GCF": ("JTF", "HJB"),
    "VHZ": ("RRN", "TSH"),
    "LNB": ("DQQ", "MQX"),
    "DRQ": ("XML", "RTK"),
    "XLG": ("LTN", "VLD"),
    "LBL": ("VVF", "SPR"),
    "MBB": ("NFG", "NFG"),
    "QJC": ("GQM", "LSB"),
    "LSR": ("BJS", "FLB"),
    "MQH": ("TJK", "KFR"),
    "DFN": ("LXG", "LLL"),
    "MSN": ("KXN", "MPV"),
    "JCT": ("MHV", "LNB"),
    "TPG": ("CJJ", "RRD"),
    "GCV": ("NVT", "SNB"),
    "LNL": ("GXX", "DJM"),
    "XFT": ("TSH", "RRN"),
    "FSS": ("SLC", "LSD"),
    "TKT": ("TVC", "LPB"),
    "XBN": ("NBX", "GCV"),
    "RQT": ("QKF", "XRS"),
    "XCC": ("MXL", "RLF"),
    "RTH": ("QVB", "MDT"),
    "DBP": ("HNV", "XCG"),
    "QQB": ("JMF", "PBJ"),
    "KSJ": ("NCS", "RNM"),
    "GNQ": ("CPX", "FXC"),
    "HHX": ("JKT", "SVM"),
    "SGG": ("KMK", "FRD"),
    "SMM": ("SJS", "PLS"),
    "VPK": ("LTM", "TKC"),
    "VLD": ("QKB", "QCZ"),
    "LTR": ("TFX", "FVN"),
    "VCL": ("DKM", "TKT"),
    "HXG": ("MTG", "SNM"),
    "KGB": ("MRV", "LFD"),
    "JGK": ("CNJ", "RXF"),
    "FMV": ("FRT", "MNF"),
    "SLD": ("KVH", "SLL"),
    "VVL": ("TNJ", "JXC"),
    "GDP": ("RBF", "KHM"),
    "XDT": ("RML", "JHK"),
    "JKP": ("NDL", "KSJ"),
    "BNH": ("SQD", "DCS"),
    "LFD": ("LQC", "HLS"),
    "NHC": ("JHT", "SSM"),
    "VPF": ("NRN", "LBL"),
    "BHT": ("LQS", "MCP"),
    "SNT": ("RHL", "BDS"),
    "BQN": ("XGL", "BLL"),
    "FVN": ("HGP", "QKM"),
    "NXC": ("KQJ", "FMV"),
    "NKG": ("SJV", "SLD"),
    "HSF": ("HPB", "NFR"),
    "QKM": ("RRR", "PMK"),
    "PJL": ("XBN", "PFX"),
    "MRP": ("LCX", "FJV"),
    "XSQ": ("FDK", "HKD"),
    "TVC": ("GHN", "QQC"),
    "XLX": ("DKJ", "NNT"),
    "VSX": ("LLL", "LXG"),
    "FQD": ("FMF", "KPC"),
    "PNJ": ("XCR", "BJT"),
    "QDV": ("QRJ", "BFS"),
    "QVG": ("GLC", "KGF"),
    "BMK": ("RJS", "FLF"),
    "SXQ": ("BQV", "RJR"),
    "BGL": ("CSB", "SBH"),
    "BJG": ("CNH", "PQJ"),
    "RSG": ("QFT", "VPD"),
    "VVF": ("DRQ", "HKC"),
    "BBT": ("LLK", "DMV"),
    "HGQ": ("GKG", "QPG"),
    "HMD": ("PHT", "PCD"),
    "PPL": ("CKL", "RCM"),
    "QLA": ("TSH", "RRN"),
    "KBG": ("HBT", "TBT"),
    "RHD": ("HKG", "SSG"),
    "GQB": ("RLF", "MXL"),
    "QFA": ("QQR", "HDH"),
    "KPC": ("BNH", "XHB"),
    "XNX": ("FVH", "MNH"),
    "HBX": ("NFD", "VJF"),
    "SVD": ("HJB", "JTF"),
    "DMD": ("JRN", "PJL"),
    "PKJ": ("BJQ", "XJJ"),
    "TFX": ("HGP", "QKM"),
    "MCH": ("PKD", "PFF"),
    "SGD": ("PKQ", "TDK"),
    "RRJ": ("KCT", "GNQ"),
    "PJD": ("VLM", "JJZ"),
    "PHF": ("PQX", "FSS"),
    "PKQ": ("NTP", "MMR"),
    "VPD": ("QHB", "NHC"),
    "FRD": ("GDP", "NVD"),
    "SFH": ("HBC", "TFR"),
    "JRN": ("XBN", "PFX"),
    "HSB": ("MRP", "LXX"),
    "RMX": ("NFD", "VJF"),
    "SBH": ("JXH", "TSQ"),
    "NTP": ("JCG", "HHX"),
    "PSX": ("FMX", "PCR"),
    "LCQ": ("PKS", "VMS"),
    "LKV": ("SMM", "PVX"),
    "SGC": ("SVD", "GCF"),
    "CQB": ("LDD", "QDV"),
    "FRT": ("XCV", "HSF"),
    "KGT": ("SGC", "VXD"),
    "TRC": ("PSX", "NQC"),
    "BSG": ("PKD", "PFF"),
    "CKB": ("FJJ", "FKD"),
    "SSM": ("JQF", "JQX"),
    "DKJ": ("BKD", "FGB"),
    "TKC": ("TXS", "FQJ"),
    "JQX": ("DVQ", "NLN"),
    "BDC": ("KNL", "DSV"),
    "FJV": ("MTJ", "XBL"),
    "DND": ("CJJ", "RRD"),
    "PPH": ("MMQ", "LDB"),
    "FTJ": ("LKT", "GNX"),
    "JKV": ("RFM", "MGK"),
    "KCR": ("LLF", "QXC"),
    "RFN": ("LJL", "CFX"),
    "HCF": ("NFG", "HSR"),
    "NTV": ("JXG", "VHP"),
    "QQR": ("DTX", "HND"),
    "BTX": ("QVG", "FDR"),
    "JQK": ("SXQ", "KQL"),
    "NJC": ("SLN", "QQH"),
    "RML": ("PDJ", "TRV"),
    "SNF": ("JDM", "CNK"),
    "KMK": ("GDP", "NVD"),
    "XSH": ("DXQ", "KNS"),
    "DTX": ("HNQ", "FSG"),
    "BNS": ("TPG", "DND"),
    "KHM": ("BFG", "VDM"),
    "SBF": ("MGK", "RFM"),
    "NFD": ("PKJ", "LDH"),
    "BHJ": ("VNN", "CGL"),
    "TXS": ("FVQ", "GKR"),
    "CRV": ("NTQ", "SDV"),
    "GHT": ("FVH", "MNH"),
    "RBN": ("RQC", "MXC"),
    "KKL": ("BDB", "CFK"),
    "NLN": ("RBN", "HBF"),
    "QFT": ("NHC", "QHB"),
    "QBL": ("FLF", "RJS"),
    "RHG": ("PNN", "CPB"),
    "MNF": ("XCV", "HSF"),
    "SJS": ("CRG", "PBL"),
    "FDK": ("VHJ", "HFH"),
    "HXM": ("JJD", "JJD"),
    "PNN": ("QDK", "MMJ"),
    "GCS": ("TTK", "NXC"),
    "VJF": ("LDH", "PKJ"),
    "GTD": ("CBR", "RJD"),
    "RRD": ("TPL", "XVR"),
    "JXC": ("LMV", "PMP"),
    "NXH": ("MKC", "CDT"),
    "HCK": ("GNX", "LKT"),
    "BRC": ("QLL", "RKH"),
    "KQB": ("CRV", "MGR"),
    "TMB": ("MCH", "BSG"),
    "XJN": ("RSX", "JGK"),
    "HQP": ("SFM", "BHT"),
    "HQT": ("MBB", "HCF"),
    "THC": ("VKN", "PHF"),
    "TPL": ("NGD", "QQB"),
    "NGD": ("PBJ", "JMF"),
    "GVJ": ("RNT", "LKV"),
    "QDK": ("LTR", "CNQ"),
    "JXG": ("QKH", "QJC"),
    "TQN": ("KRL", "QCV"),
    "RDB": ("JQS", "BRC"),
    "MPV": ("LRL", "QKK"),
    "SJQ": ("HKG", "SSG"),
    "XHL": ("RNL", "FHV"),
    "LRF": ("KQB", "FPK"),
    "GNX": ("SSC", "VPF"),
    "VXV": ("XLX", "RDT"),
    "MTG": ("CCR", "CRR"),
    "NFG": ("BHH", "BHH"),
    "DSV": ("PXB", "PJN"),
    "CVT": ("KPT", "DBF"),
    "RHL": ("JTM", "XJK"),
    "CBQ": ("GXL", "PQB"),
    "BHH": ("JXS", "MFQ"),
    "DMV": ("BDC", "PNK"),
    "NSS": ("HQP", "LBS"),
    "FVM": ("PRP", "RFN"),
    "NCS": ("HTP", "LVL"),
    "QPD": ("NDT", "SLM"),
    "GJC": ("FDR", "QVG"),
    "CFK": ("JGG", "NMP"),
    "HDV": ("MGD", "DBP"),
    "PNB": ("PQB", "GXL"),
    "RXA": ("NLJ", "JPG"),
    "CNH": ("JSF", "BQQ"),
    "VXL": ("HXR", "XQQ"),
    "QKF": ("RDP", "DHT"),
    "QTS": ("QKF", "XRS"),
    "VDL": ("SGD", "FRJ"),
    "FCM": ("TQN", "GXV"),
    "BHQ": ("GQC", "QRR"),
    "BSD": ("FTJ", "HCK"),
    "CJJ": ("TPL", "XVR"),
    "PLG": ("DTD", "BSD"),
    "LQC": ("TKM", "TJQ"),
    "NTM": ("KLG", "PPL"),
    "SHJ": ("NRL", "NMS"),
    "QDL": ("BDS", "RHL"),
    "PCR": ("XFP", "QKX"),
    "XCG": ("XFH", "BKL"),
    "LMV": ("GCS", "PXP"),
    "JJD": ("QQV", "QQV"),
    "HGP": ("PMK", "RRR"),
    "TNF": ("RQT", "QTS"),
    "SFM": ("MCP", "LQS"),
    "MNR": ("RFN", "PRP"),
    "LLL": ("CBQ", "PNB"),
    "RJS": ("SNF", "KRN"),
    "BRV": ("CVV", "DDS"),
    "GGK": ("LHS", "PLG"),
    "HVD": ("GBJ", "VQQ"),
    "KQJ": ("FRT", "MNF"),
    "PMK": ("CGR", "PQR"),
    "MFB": ("GGK", "CLL"),
    "HLK": ("NTG", "KMB"),
    "BKL": ("CQL", "DVM"),
    "SVT": ("CSB", "SBH"),
    "FGD": ("PNR", "NCV"),
    "LVT": ("VCL", "XTQ"),
    "MFQ": ("SBL", "CQB"),
    "SCC": ("KKH", "LBH"),
    "JMF": ("VFB", "LTK"),
    "GLC": ("FBS", "DNB"),
    "HFT": ("MMQ", "LDB"),
    "PNR": ("PTG", "KSB"),
    "SNM": ("CRR", "CCR"),
    "TJK": ("DTV", "KPD"),
    "PQR": ("NJC", "CNF"),
    "VPM": ("QDL", "SNT"),
    "DHT": ("KGT", "CXH"),
    "RPK": ("KML", "XRL"),
    "VFH": ("HSB", "QBV"),
    "FNP": ("JBQ", "JKP"),
    "JLS": ("QLN", "JCS"),
    "XMS": ("JGK", "RSX"),
    "FRK": ("GGK", "CLL"),
    "PDJ": ("GKF", "BVN"),
    "QDH": ("JLC", "QTG"),
    "PFX": ("GCV", "NBX"),
    "BXB": ("MBB", "MBB"),
    "TTK": ("KQJ", "FMV"),
    "PKS": ("DDC", "CTJ"),
    "KLG": ("RCM", "CKL"),
    "CSV": ("QVB", "MDT"),
    "NNG": ("DXR", "BPD"),
    "HHC": ("KCR", "QJP"),
    "LVL": ("CSQ", "TKJ"),
    "QHB": ("JHT", "SSM"),
    "JDM": ("SKK", "NFL"),
    "JCQ": ("TNK", "LPJ"),
    "TSQ": ("MQH", "PRD"),
    "JTS": ("PQJ", "CNH"),
    "RCR": ("KCT", "GNQ"),
    "LXG": ("CBQ", "PNB"),
    "TKQ": ("HXP", "TNF"),
    "PKM": ("PBT", "SJR"),
    "GXV": ("QCV", "KRL"),
    "HJS": ("BBX", "RPK"),
    "CPX": ("XSK", "XSK"),
    "JXD": ("BTX", "GJC"),
    "CVV": ("HXM", "VDB"),
    "SBL": ("LDD", "QDV"),
    "HBC": ("VPM", "KKG"),
    "DXR": ("CVT", "KKS"),
    "VDB": ("JJD", "BVS"),
    "XQQ": ("VVL", "LRZ"),
    "PQB": ("BXS", "XSQ"),
    "NTX": ("HXP", "TNF"),
    "SCG": ("VMQ", "HJS"),
    "GHN": ("SBF", "JKV"),
    "VXR": ("SGL", "LMC"),
    "NQF": ("VPD", "QFT"),
    "DDS": ("HXM", "VDB"),
    "KLM": ("LBH", "KKH"),
    "SGL": ("QRL", "KLQ"),
    "GKR": ("CSV", "RTH"),
    "QDT": ("DFN", "VSX"),
    "MNT": ("SNH", "FPP"),
    "TDP": ("TKV", "KVP"),
    "KNL": ("PXB", "PXB"),
    "GMN": ("KVP", "TKV"),
    "MXL": ("SGG", "LCR"),
    "PKD": ("FXX", "KVK"),
    "SXP": ("FNK", "VPK"),
    "NTG": ("BSX", "FDM"),
    "QSR": ("KBG", "CKD"),
    "FHV": ("XCL", "MBP"),
    "RDT": ("NNT", "DKJ"),
    "SPR": ("HKC", "DRQ"),
    "FFN": ("JHD", "GLR"),
    "FBS": ("QXL", "FTF"),
    "VLP": ("FFN", "NKT"),
    "KXC": ("SKL", "GVJ"),
    "TKJ": ("FQR", "FGD"),
    "LHH": ("PHT", "PCD"),
    "CTM": ("GHV", "QMV"),
    "VHH": ("JQS", "BRC"),
    "MQX": ("MJM", "QQS"),
    "BBX": ("XRL", "KML"),
    "LKK": ("PKM", "FPN"),
    "RNT": ("PVX", "SMM"),
    "JSA": ("TNJ", "JXC"),
    "RDK": ("LBS", "HQP"),
    "RXF": ("MNT", "DCG"),
    "HDH": ("HND", "DTX"),
    "VKN": ("FSS", "PQX"),
    "LSB": ("VLP", "BXQ"),
    "BPD": ("CVT", "KKS"),
    "TMT": ("BSG", "MCH"),
    "QLV": ("JBQ", "JKP"),
    "LPJ": ("KVD", "QSX"),
    "QDS": ("VPK", "FNK"),
    "GQS": ("VXV", "DNL"),
    "DTV": ("NSS", "RDK"),
    "SNB": ("JLB", "LLV"),
    "NMM": ("SXP", "QDS"),
    "CSB": ("TSQ", "JXH"),
    "PFF": ("FXX", "KVK"),
    "VHJ": ("XDV", "DMD"),
    "XFX": ("KSN", "THB"),
    "CCR": ("NQF", "RSG"),
    "VMQ": ("BBX", "RPK"),
    "HXR": ("VVL", "VVL"),
    "SJV": ("KVH", "SLL"),
    "CFN": ("KLG", "PPL"),
    "DDH": ("RHG", "GJN"),
    "FLG": ("HMD", "LHH"),
    "FVQ": ("RTH", "CSV"),
    "RTK": ("BMK", "QBL"),
    "NSC": ("SVH", "QSR"),
    "MKC": ("FCM", "JKR"),
    "XTJ": ("GHV", "QMV"),
    "CNQ": ("FVN", "TFX"),
    "SJR": ("BJJ", "BHQ"),
    "MGR": ("NTQ", "SDV"),
    "XFH": ("DVM", "CQL"),
    "QSX": ("GRR", "PNJ"),
    "QKX": ("HBX", "RMX"),
    "LBK": ("BQN", "BRT"),
    "PXQ": ("MRV", "LFD"),
    "LDQ": ("SFH", "RHV"),
    "MNH": ("HHC", "TSV"),
    "XCV": ("HPB", "NFR"),
    "KLQ": ("QBJ", "XSH"),
    "FTF": ("SCQ", "RGC"),
    "JJQ": ("MPV", "KXN"),
    "LJL": ("VDV", "SJJ"),
    "DNB": ("FTF", "QXL"),
    "CFX": ("VDV", "SJJ"),
    "JKT": ("DKT", "DKT"),
    "SJJ": ("THK", "HSK"),
    "CDL": ("JLS", "CPK"),
    "QCV": ("XRH", "LKK"),
    "XCR": ("GJL", "JXD"),
    "KMJ": ("MLJ", "PQZ"),
    "MPS": ("DJM", "GXX"),
    "GBJ": ("MQN", "FQD"),
    "PNK": ("KNL", "DSV"),
    "BRB": ("HMD", "LHH"),
    "PBT": ("BJJ", "BHQ"),
    "JPG": ("JCT", "GBH"),
    "HSR": ("BHH", "ZZZ"),
    "DQQ": ("QQS", "MJM"),
    "MCP": ("SJQ", "RHD"),
    "LTM": ("TXS", "FQJ"),
    "KKS": ("KPT", "DBF"),
    "DCG": ("FPP", "SNH"),
    "TDK": ("MMR", "NTP"),
    "QJP": ("LLF", "QXC"),
    "NFR": ("FNQ", "VHR"),
    "FKD": ("FNT", "VXL"),
    "LMC": ("KLQ", "QRL"),
    "PBL": ("FVM", "MNR"),
    "JHD": ("DMF", "HVD"),
    "CRR": ("RSG", "NQF"),
    "JJZ": ("JVD", "JSN"),
    "RQH": ("DXR", "BPD"),
    "HXF": ("VCL", "XTQ"),
    "CRG": ("MNR", "FVM"),
    "VHR": ("QHG", "LCQ"),
    "VCS": ("VTX", "TGX"),
    "FPP": ("QDH", "PSQ"),
    "KSN": ("XFT", "XFT"),
    "BVS": ("QQV", "PJD"),
    "RSX": ("RXF", "CNJ"),
    "FXC": ("XSK", "XFX"),
    "HDJ": ("CDL", "VGL"),
    "QQC": ("SBF", "JKV"),
    "LPB": ("GHN", "QQC"),
    "LRJ": ("QHS", "JQK"),
    "SCQ": ("RCR", "RRJ"),
    "PQJ": ("JSF", "BQQ"),
    "GKG": ("VMJ", "LRJ"),
    "SSC": ("NRN", "LBL"),
    "NVT": ("JLB", "LLV"),
    "KVD": ("GRR", "PNJ"),
    "XRL": ("CTT", "MCX"),
    "BTS": ("VMQ", "HJS"),
    "KRL": ("XRH", "LKK"),
    "RRN": ("BGL", "SVT"),
    "FHS": ("SNM", "MTG"),
    "QPG": ("VMJ", "LRJ"),
    "QKK": ("TRC", "MCG"),
    "VDV": ("THK", "HSK"),
    "GPH": ("VXR", "GKQ"),
    "RNL": ("XCL", "MBP"),
    "SLN": ("THC", "THR"),
    "CPB": ("MMJ", "QDK"),
    "NMS": ("XTJ", "CTM"),
    "RJR": ("BTS", "SCG"),
    "CGL": ("VCS", "BSR"),
    "MBP": ("MFB", "FRK"),
    "NNT": ("FGB", "BKD"),
    "HTP": ("CSQ", "TKJ"),
    "GPG": ("RML", "JHK"),
    "QRL": ("QBJ", "XSH"),
    "BCD": ("GSV", "QPD"),
    "QQV": ("VLM", "VLM"),
    "PRP": ("CFX", "LJL"),
    "TFR": ("KKG", "VPM"),
    "LDD": ("QRJ", "BFS"),
    "QVM": ("VNN", "CGL"),
    "KGF": ("FBS", "DNB"),
    "GBH": ("MHV", "LNB"),
    "JCG": ("JKT", "SVM"),
    "FJQ": ("NMS", "NRL"),
    "QXL": ("RGC", "SCQ"),
    "NRN": ("SPR", "VVF"),
    "FDM": ("XMS", "XJN"),
    "RFM": ("BRV", "CRH"),
    "NKT": ("GLR", "JHD"),
    "HFR": ("VHD", "LBJ"),
    "THB": ("XFT", "VHZ"),
    "XJJ": ("BXB", "HQT"),
    "QTG": ("VSV", "TKN"),
    "NQC": ("PCR", "FMX"),
    "JLB": ("HFT", "PPH"),
    "GXL": ("BXS", "XSQ"),
    "PSQ": ("QTG", "JLC"),
    "NDT": ("BRB", "FLG"),
    "PJN": ("RRT", "KMJ"),
    "TBT": ("CKB", "CCX"),
    "JBH": ("GKQ", "VXR"),
    "XVR": ("QQB", "NGD"),
    "BRT": ("XGL", "BLL"),
    "PCD": ("MPS", "LNL"),
    "SKL": ("RNT", "LKV"),
    "TSH": ("BGL", "SVT"),
    "JQF": ("DVQ", "NLN"),
    "DVQ": ("RBN", "HBF"),
    "RGC": ("RCR", "RRJ"),
    "QRJ": ("TNL", "NXH"),
    "XCL": ("MFB", "FRK"),
    "VLM": ("JSN", "JVD"),
    "RDP": ("KGT", "CXH"),
    "VTJ": ("FLB", "BJS"),
    "LCX": ("XBL", "MTJ"),
    "JVD": ("QFQ", "LJQ"),
    "BKM": ("NJK", "PBD"),
    "VMJ": ("QHS", "JQK"),
    "DMF": ("VQQ", "GBJ"),
    "CDT": ("FCM", "JKR"),
    "NTQ": ("NTV", "VMG"),
    "QRR": ("NSF", "NKG"),
    "NDL": ("RNM", "NCS"),
    "KVG": ("LPJ", "TNK"),
    "DCS": ("BLK", "LBK"),
    "JFQ": ("RHG", "GJN"),
    "GKQ": ("SGL", "LMC"),
    "JTF": ("GPG", "XDT"),
    "SVH": ("CKD", "KBG"),
    "RRR": ("PQR", "CGR"),
    "RHN": ("CHN", "XHL"),
    "HNQ": ("GPH", "JBH"),
    "BFG": ("GTD", "HRP"),
    "LLV": ("PPH", "HFT"),
    "NMP": ("BJG", "JTS"),
    "CSQ": ("FQR", "FGD"),
    "MRV": ("HLS", "LQC"),
    "LDJ": ("KMB", "NTG"),
    "PHT": ("LNL", "MPS"),
    "DJM": ("RCJ", "KKL"),
    "PTG": ("VBD", "VDL"),
    "PMP": ("PXP", "GCS"),
    "LTN": ("QKB", "QKB"),
    "BFS": ("NXH", "TNL"),
    "MGD": ("XCG", "HNV"),
    "QBV": ("MRP", "LXX"),
    "VFB": ("LVT", "HXF"),
    "XTQ": ("TKT", "DKM"),
    "QBR": ("QBV", "HSB"),
    "CPK": ("QLN", "JCS"),
    "MCG": ("NQC", "PSX"),
    "VMG": ("VHP", "JXG"),
    "FNQ": ("LCQ", "QHG"),
}
inputNav = "LRRLRRLRRLRRRLRRLRRRLRRLRRRLRLRLLRLRLRRLLLRLRLRRRLRRLRLRRRLRRLRRLRRLLLRRLRRRLRRRLRLLRRLRLLRRLRRRLRRLRLRRRLRLRLRRLRLRRRLLRRRLLRRRLRLRRRLRRLLRRLRRRLRRLRRLLRRLRRLRRRLLLRRRLRRLRRLRRLRLRRRLRRLLLLRLRRLRRRLRLLRRLRLLRRLRRRLRRRLRRRLLRRLRRLRRLRRRLRRLRRRLLRLRRRLRRRLRRRLLRRRLRRLRRRR"
inputStart = ["AAA", "RLA", "QLA", "QFA", "RXA", "JSA"]

def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

def step(curr, dir, network):
    node = ""
    if dir == "L":
        node = network[curr][0]
    elif dir == "R":
        node = network[curr][1]
    
    return node

def atEnd(curr):
    for item in curr:
        if item[-1:] != "Z":
            return False
    
    return True

def navigate(nav, network, start):
    found = False
    curr = network[start]
    node = start
    count = 0

    while not found:
        for dir in nav:
            count += 1
            if dir == "L":
                node = curr[0]
            elif dir == "R":
                node = curr[1]
            
            if node[-1] == "Z":
                found = True
                break

            curr = network[node]

    return count

if __name__ == '__main__':
    result = 0
    loop = []

    for start in inputStart:
        loop.append(navigate(inputNav, input, start))
    result = reduce(lcm, loop)

    print(result)
