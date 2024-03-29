MASTER_STEPS_UDFS = {
    "received": {
        "steps": [
            "CG002 - Reception Control (Dev)",
            "CG002 - Reception Control",
            "Reception Control TWIST v1",
            "Reception Control no placement v1",
            "Reception Control (RNA) v1",
            "Reception Control (Dev) v3",
        ],
        "date_udf": "date arrived at clinical genomics",
    },
    "prepared": {
        "steps": [
            "CG002 - Aggregate QC (Library Validation) (Dev)",
            "Aggregate QC (Library Validation) (Dev) v3",
            "CG002 - Aggregate QC (Library Validation)",
            "Aggregate QC (Library Validation) TWIST v1",
            "Aggregate QC (Library Validation) (RNA) v2",
            "Aggregate QC (Library Validation)",
        ]
    },
    "delivery": {"steps": ["CG002 - Delivery", "Delivery v1"], "date_udf": "Date delivered"},
    "sequenced": {
        "steps": [
            "CG002 - Illumina Sequencing (HiSeq X)",
            "CG002 - Illumina Sequencing (Illumina SBS)",
            "AUTOMATED - NovaSeq Run",
        ],
        "date_udf": "Finish Date",
        "nova_seq": ["AUTOMATED - NovaSeq Run"],
        "q30r1_udf": "% Bases >=Q30 R1",
        "q30r2_udf": "% Bases >=Q30 R2",
    },
    "concentration_and_nr_defrosts": {
        "lot_nr_step": [
            "CG002 - End repair Size selection A-tailing and Adapter ligation (TruSeq PCR-free DNA)",
            "End repair Size selection A-tailing and Adapter ligation (TruSeq PCR-free DNA)",
        ],
        "concentration_step": [
            "CG002 - Aggregate QC (Library Validation)",
            "Aggregate QC (Library Validation)",
        ],
        "lot_nr_udf": "Lot no: TruSeq DNA PCR-Free Sample Prep Kit",
        "concentration_udf": "Concentration (nM)",
        "apptags": ["WGSPCF", "WGTPCF", "WGLPCF"],
    },
    "final_conc_and_amount_dna": {
        "amount_udf": "Amount (ng)",
        "concentration_udf": "Concentration (nM)",
        "concentration_step": [
            "CG002 - Aggregate QC (Library Validation)",
            "Aggregate QC (Library Validation)",
        ],
        "amount_step": ["CG002 - Aggregate QC (DNA)", "Aggregate QC (DNA)"],
        "apptags": ["WGSLIF", "WGTLIF", "WGLLIF"],
    },
    "microbial_library_concentration": {
        "concentration_step": "CG002 - Aggregate QC (Library Validation)",
        "concentration_udf": "Concentration (nM)",
        "apptags": "NX",
    },
    "library_size_pre_hyb": {
        "TWIST": {
            "size_step": ["pool samples TWIST v1"],
            "stage_udf": {"3999": "Size (bp)", "2176": "Average Size (bp)"},
        },
        "SureSelect": {
            "size_step": ["CG002 - Amplify Adapter-Ligated Library (SS XT)"],
            "size_udf": "Size (bp)",
            "apptags": ["EXO", "EFT", "PAN", "PAL"],
        },
    },
    "library_size_post_hyb": {
        "TWIST": {
            "size_step": ["CG002 - Sort HiSeq Samples"],
            "stage_udf": {"4005": "Size (bp)", "2182": "Average Size (bp)"},
        },
        "SureSelect": {
            "size_step": ["CG002 - Amplify Captured Libraries to Add Index Tags (SS XT)"],
            "size_udf": "Size (bp)",
            "apptags": ["EXO", "EFT", "PAN", "PAL"],
        },
    },
    "reagent_labels": {
        "steps": {
            "bcl": ["Bcl Conversion & Demultiplexing (Nova Seq)"],
            "define": ["Define Run Format and Calculate Volumes (Nova Seq)"],
            "pre_bcl": ["STANDARD Prepare for Sequencing (Nova Seq)"],
        },
        "udfs": {"reads": "# Reads", "target_reads": "Reads to sequence (M)"},
        "exclue_tags": ["RM", "EX", "PA"]
        ## EX and PA should be included later. Fetching fraction from Poos Samples Twist 1
    },
}

INSTRUMENTS = {
    "D00410": "Sigourney",
    "D00415": "Merida",
    "D00450": "Arnold",
    "ST-E00198": "Dorothy",
    "ST-E00201": "Irene",
    "ST-E00214": "Marie",
    "ST-E00266": "Rita",
    "ST-E00269": "Rosalyn",
    "A00187": "Ingrid",
    "A00689": "Barbara",
    "A00621": "Greta",
    "FS10000534": "Katherine",
}

TEST_SAMPLES = [
    "SIB603A6",
    "ADM1852A2",
    "SIB603A3",
    "SER305A1",
    "AND51A3",
    "BRA1907A5",
    "SIB552A11",
    "SIB603A9",
    "SIB257A27",
    "SIB552A15",
    "SIB611A3",
    "SIB552A16",
    "SIB256A3",
    "SIB601A5",
    "SIB553A24",
    "SIB404A15",
    "SIB404A13",
    "SIB663A2",
    "SIB701A1",
    "SIB552A18",
    "SIB257A26",
    "SER303A1",
    "SIB553A27",
    "SIB257A23",
    "SIB607A1",
    "SIB603A2",
    "SIB404A14",
    "SIB403A27",
    "SIB603A12",
    "SIB603A14",
    "SIB601A11",
    "SER305A2",
    "SIB663A4",
    "ADM1852A1",
    "SIB552A12",
    "SIB552A13",
    "SIB552A10",
    "SIB553A19",
    "SIB553A10",
    "SIB553A15",
    "SIB603A8",
    "SIB603A4",
    "SIB553A17",
    "SIB603A16",
    "SIB652A1",
    "SIB552A3",
    "SIB552A4",
    "SIB601A7",
    "SIB553A28",
    "SIB552A2",
    "SIB603A18",
    "BRA1907A1",
    "SIB404A17",
    "SIB404A16",
    "SIB553A3",
    "SIB256A1",
    "BIL1393A1",
    "SIB601A1",
    "SIB603A10",
    "SER305A5",
    "SIB603A5",
    "SER305A4",
    "ADM1851A4",
    "SER305A6",
    "SER307A8",
    "BRA1907A4",
    "BRA1907A3",
    "SIB601A4",
    "SER307A7",
    "BRA1907A2",
    "SIB257A25",
    "SIB603A13",
    "SIB601A12",
    "SIB601A14",
    "SER305A7",
    "SIB552A17",
    "SIB256A2",
    "SIB553A14",
    "SIB601A2",
    "SIB553A12",
    "SIB603A20",
    "SIB553A13",
    "SIB553A9",
    "SIB404A19",
    "ADM1852A3",
    "SIB606A2",
    "SIB404A18",
    "SIB552A5",
    "SIB603A1",
    "SIB552A6",
    "SER305A3",
    "SIB552A8",
    "SIB351A22",
    "SER307A4",
    "SIB603A15",
    "SER305A8",
    "SIB603A19",
    "SIB553A7",
    "SIB611A1",
    "SIB553A8",
    "SIB553A5",
    "SER303A3",
    "SIB351A21",
    "SIB553A16",
    "SIB255A1",
    "SIB608A1",
    "SIB351A24",
    "SIB501A2",
    "SIB403A25",
    "SIB501A3",
    "SER303A7",
    "SIB603A11",
    "AND51A4",
    "SIB553A25",
    "SIB502A2",
    "SIB501A4",
    "SER303A8",
    "SIB652A2",
    "SIB257A24",
    "AND51A1",
    "BRA1907A6",
    "AND51A5",
    "SIB501A1",
    "SIB601A8",
    "SIB257A22",
    "SIB653A1",
    "SER307A2",
    "SER303A6",
    "SIB351A20",
    "SER307A3",
    "SIB553A6",
    "ADM1852A4",
    "SIB601A6",
    "SIB404A21",
    "SER303A4",
    "SER303A5",
    "SER303A2",
    "SIB601A10",
    "SIB553A26",
    "SER307A5",
    "SIB553A1",
    "SIB253A1",
    "SIB351A23",
    "SIB253A2",
    "SIB404A22",
    "SIB601A3",
    "SIB553A4",
    "SIB702A1",
    "ADM1851A3",
    "SIB552A14",
    "AND51A6",
    "SIB609A1",
    "SER307A6",
    "SIB606A1",
    "SIB611A2",
    "SIB553A22",
    "SIB255A3",
    "SIB603A17",
    "SIB253A3",
    "ADM1851A2",
    "SIB601A13",
    "SIB553A18",
    "AND51A2",
    "SIB403A26",
    "SIB552A9",
    "SIB553A2",
    "SIB553A20",
    "SER307A1",
    "SIB553A21",
    "SIB404A20",
    "SIB663A3",
    "SIB404A24",
    "ADM990A1",
    "SIB603A7",
    "SIB404A23",
    "SIB553A23",
    "SIB552A7",
    "SIB502A1",
    "SIB351A19",
    "SIB552A1",
    "SIB601A9",
    "ADM1851A1",
    "SIB553A11",
    "SIB255A2",
]

LANE_UDFS = [
    "Clusters PF R1",
    "Clusters PF R2",
    "% Aligned R1",
    "% Aligned R2",
    "% Bases >=Q30",
    "% Bases >=Q30 R1",
    "% Bases >=Q30 R2",
    "% Error Rate R1",
    "% Error Rate R2",
    "% Phasing R1",
    "% Prephasing R1",
    "% Prephasing R2",
    "%PF R1",
    "%PF R2",
    "Cluster Density (K/mm^2) R1",
    "Cluster Density (K/mm^2) R2",
    "Intensity Cycle 1 R1",
    "Intensity Cycle 1 R2",
    "Reads PF (M) R1",
    "Reads PF (M) R2",
    "Yield PF (Gb) R1",
    "Yield PF (Gb) R2",
    "% Phasing R2",
]
