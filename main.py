from get_data import get_healthy_7
from multikernel import MultiKernelDevice

def get_triplets(patient, component, lead_name='i'):
    return patient['Leads'][lead_name]['DelineationDoc'][component]

def handle_ecg_to_3_device(ecg_json, device1, device2, device3):
    i_qrs_triplets = get_triplets(ecg_json, "qrs", "i")
    for triplet in i_qrs_triplets:
        left = triplet[0]
        center = triplet[1]
        right = triplet[2]
        print (str(left - right)) # mean 40

if __name__ == "__main__":
    json_data = get_healthy_7()
    max_distance = 20
    ker_size = 10
    device1 = MultiKernelDevice(max_distance, ker_size)
    device2 = MultiKernelDevice(max_distance, ker_size)
    device3 = MultiKernelDevice(max_distance, ker_size)
    for patient_id in json_data.keys():
        patient = json_data[patient_id]
        handle_ecg_to_3_device(patient, device1, device2, device3)
