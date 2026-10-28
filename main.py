
import os
import requests
from dotenv import load_dotenv

API_URL = "https://core.bloxgen.net/api/generate"


def load_keys():
    load_dotenv()
    keys = {}

    for i in range(1, 101):
        key = os.getenv(f"BLOXGEN_API_KEY_{i}", "").strip()
        if key:
            keys[i] = key

    return keys


def generate_account(api_key, account_type):
    response = requests.post(
        API_URL,
        json={
            "apiKey": api_key,
            "type": account_type
        },
        headers={
            "Content-Type": "application/json"
        },
        timeout=30
    )

    try:
        result = response.json()
    except ValueError:
        raise RuntimeError(
            f"Respons bukan JSON. HTTP {response.status_code}"
        )

    if not response.ok or not result.get("success"):
        message = (
            result.get("message")
            or result.get("error")
            or "Request gagal."
        )
        raise RuntimeError(
            f"HTTP {response.status_code}: {message}"
        )

    return result.get("data", {})


def main():
    keys = load_keys()

    if not keys:
        print("API Key tidak ditemukan di file .env!")
        print("Isi BLOXGEN_API_KEY_1 dan seterusnya.")
        return

    print("=" * 35)
    print("       BLOXGEN API CLIENT")
    print("=" * 35)

    print("\nAPI Key tersedia:")
    for number in keys:
        print(f"  {number}. API Key #{number} (disembunyikan)")

    try:
        selected = int(input("\nPilih nomor API Key: "))
    except ValueError:
        print("Masukkan nomor yang valid.")
        return

    api_key = keys.get(selected)

    if not api_key:
        print("Nomor API Key tidak ditemukan.")
        return

    account_type = input("Tipe akun [alt]: ").strip() or "alt"

    if not account_type.replace("+", "").replace("-", "").replace("_", "").isalnum():
        print("Format tipe akun tidak valid.")
        return

    print(f"\nTipe akun: {account_type}")
    print("API Key: disembunyikan")

    confirm = input("Lanjut generate satu akun? [y/N]: ").strip().lower()

    if confirm != "y":
        print("Generate dibatalkan.")
        return

    try:
        print("\nMengirim request...")

        account = generate_account(api_key, account_type)

        print("\n[BERHASIL]")
        print("Username :", account.get("username", "-"))
        print("Account ID:", account.get("id", "-"))
        print("Type     :", account.get("type", "-"))
        print("Cost     :", account.get("cost", "-"))

        print("\nPassword dan cookie tidak ditampilkan.")

    except requests.RequestException as error:
        print("\nKoneksi gagal:", error)

    except RuntimeError as error:
        print("\nGenerate gagal:", error)


if __name__ == "__main__":
    main()
