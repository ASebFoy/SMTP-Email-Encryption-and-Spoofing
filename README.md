# SMTP Email Encryption and Spoofing Demonstration

## Scenario
This lab demonstrates how email encryption (OpenPGP) works in practice, how unencrypted messages can be intercepted, and how spoofed encrypted messages can still mislead recipients if sender verification is not enforced.

In this demonstration:
- A local mail server (hMailServer) is configured with fictional users such as `John.Insider@gov.local` and `Jane.Journalist@gov.local`.
- Thunderbird is set up with OpenPGP encryption using keys generated via Kleopatra.
- An unencrypted email is sent, received, and intercepted in Wireshark to show plaintext exposure.
- An encrypted email is sent, received, and inspected in Wireshark to show unreadable ciphertext.
- A bad actor crafts a spoofed encrypted message, scripts it in Python, and sends it over SMTP to the victim.
- The spoofed message is intercepted in Wireshark, showing that encryption alone does not prove sender authenticity.

## Tools and Environment
Mail Server: hMailServer (local instance)
Email Client: Mozilla Thunderbird with OpenPGP support
Network Analysis: Wireshark
Encryption Utility: Kleopatra (OpenPGP)
Scripting: Python for SMTP spoofing

## Project Structure

/screenshots
Ordered step-by-step images of the demonstration

/keys
Public keys for fictional users John Insider and Jane Journalist

/scripts
Python script used for sending spoofed encrypted emails

README.md

## Steps

1. Configure the Mail Server  
   *step01-hmailserver-domain.png*  
   Configure hMailServer locally with the domain `gov.local`.

2. Generate PGP Keypair  
   *step02-generate-pgp-key.png*  
   Create an OpenPGP keypair using Kleopatra and import it into Thunderbird.

3. Add Account in Thunderbird  
   *step03-thunderbird-account-setup.png*  
   Create the email account in Thunderbird.

4. Enable OpenPGP in Thunderbird  
   *step04-enable-openpgp-thunderbird.png*  
   Ensure the generated PGP key is linked to the Thunderbird account.

5. Compose a Plaintext Email  
   *step05-compose-plaintext-email.png*  
   Write an unencrypted email.

6. Receive the Plaintext Email  
   *step06-receive-plaintext-unverified.png*  
   The recipient sees the message without verification.

7. Intercept the Plaintext in Wireshark  
   *step07-wireshark-plaintext-follow-stream.png*  
   Capture and follow the TCP stream to read the message contents.

8. Compose an Encrypted Email  
   *step08-compose-encrypted-email.png*  
   Send the same email but with encryption enabled.

9. Receive the Encrypted Email  
   *step09-receive-encrypted-verified.png*  
   The recipient sees a verified encrypted message.

10. Intercept the Encrypted Message in Wireshark  
    *step10-wireshark-encrypted-follow-stream.png*  
    The captured content appears as unreadable ciphertext.

11. Bad Actor Creates a Spoofed Encrypted Message  
    *step11-gpg-encrypt-command.png*  
    The attacker uses the recipient’s public key to encrypt their own malicious text.

12. Bad Actor Crafts a Spoofed Email in Python  
    *step12-python-smtp-with-asc.png*  
    In a Python script, the attacker embeds the malicious encrypted text into a spoofed SMTP message to make it appear as if it came from a trusted contact.

13. Bad Actor Sends the Spoofed Email  
    *step13-run-python-send.png*  
    The spoofed encrypted message is sent to the victim.

14. Receive the Spoofed Encrypted Email  
    *step14-receive-spoofed-unverified.png*  
    The message appears encrypted but without sender verification.

## Mitigations
- Use digital signatures to verify sender authenticity.
- Enforce strict PGP key verification policies in email clients.
- Monitor and filter SMTP traffic for spoofing attempts.
- Educate users that encryption does not guarantee the identity of the sender.

## Disclaimer
This project is intended for educational purposes only. All individuals, domains, and keys are fictional. No real systems, accounts, or data were accessed. Do not attempt this outside of a controlled lab environment with explicit permission.
