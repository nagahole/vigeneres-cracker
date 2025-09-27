## Vigenère Cipher Cracking

### Approach

I began by searching for repeating substrings in the ciphertext to apply the **Kasiski test**.  
Substrings shorter than three characters appeared too often to be useful, so I restricted the search to lengths **3–10** and listed them by frequency. The most common were `JEW`, `NZF`, and `YTD`, which I highlighted using **Colorama** for easier inspection.

Initial attempts to directly substitute common trigrams like `THE` and `AND` were unhelpful. Instead, I measured the gaps between repeated substrings and used their common factors to deduce the **key length as 17**.  

I then split the ciphertext into 17 columns (one per key position) and applied frequency analysis. This revealed the first six key characters, producing partial plaintext when tested. From there, I completed the key by contextually guessing likely words (e.g. `RMMO → MANY`, `ZKE → HOW`).

With all 17 characters determined, decrypting the ciphertext yielded a fully legible English plaintext, confirming the correct keyword.

- **Key length:** 17  
- **Key:** `XVFERTQXSWIFMZQAB`

### Final Plaintext

NO MATTER HOW MANY TIMES YOU LEFT EARTH, DR. HEYWOOD FLOYD TOLD HIMSELF, THE EXCITEMENT NEVER
REALLY PALLED. HE HAD BEEN TO MARS ONCE, TO THE MOON THREE TIMES, AND TO THE VARIOUS SPACE
STATIONS MORE OFTEN THAN HE COULD REMEMBER. YET AS THE MOMENT OF TAKEOFF APPROACHED, HE WAS
CONSCIOUS OF A RISING TENSION, A FEELING OF WONDER AND AWE - YES; AND OF NERVOUSNESS - WHICH
PUT HIM ON THE SAME LEVEL AS ANY EARTHLUBBER ABOUT TO RECEIVE HIS FIRST BAPTISM OF SPACE. THE
JET THAT HAD RUSHED HIM HERE FROM WASHINGTON, AFTER THAT MIDNIGHT BRIEFING WITH THE
PRESIDENT, WAS NOW DROPPING DOWN TOWARD ONE OF THE MOST FAMILIAR, YET MOST EXCITING,
LANDSCAPES IN ALL THE WORLD. THERE LAY THE FIRST TWO GENERATIONS OF THE SPACE AGE, SPANNING
TWENTY MILES OF THE FLORIDA COAST TO THE SOUTH, OUTLINED BY WINKING RED WARNING LIGHTS, WERE
THE GIANT GANTRIES OF THE SATURNS AND NEPTUNES, THAT HAD SET MEN ON THE PATH TO THE PLANETS,
AND HAD NOW PASSED INTO HISTORY. CYBERSECURITY ENGINEERING ASSIGNMENT. NEAR THE HORIZON, A
GLEAMING SILVER TOWER BATHED IN FLOODLIGHTS, STOOD THE LAST OF THE SATURN V’S, FOR ALMOST
TWENTY YEARS A NATIONAL MONUMENT AND PLACE OF PILGRIMAGE. NOT FAR AWAY, LOOMING AGAINST THE
SKY LIKE A MAN-MADE MOUNTAIN, WAS THE INCREDIBLE BULK OF THE VEHICLE ASSEMBLY BUILDING, STILL
THE LARGEST SINGLE STRUCTURE ON EARTH. BUT THESE THINGS NOW BELONGED TO THE PAST, AND HE WAS
FLYING TOWARD THE FUTURE. AS THEY BANKED, DR. FLOYD COULD SEE BELOW HIM A MAZE OF BUILDINGS,
THEN A GREAT AIRSTRIP, THEN A BROAD, DEAD-STRAIGHT SCAR ACROSS THE FLAT FLORIDA LANDSCAPE -
THE MULTIPLE RAILS OF A GIANT LAUNCH-LUG TRACK. AT ITS END, SURROUNDED BY VEHICLES AND
GANTRIES, A SPACEPLANE LAY GLEAMING IN A POOL OF LIGHT, BEING PREPARED FOR ITS LEAP TO THE
STARS. IN A SUDDEN FAILURE OF PERSPECTIVE, BROUGHT ON BY HIS SWIFT CHANGES OF SPEED AND
HEIGHT, IT SEEMED TO FLOYD THAT HE WAS LOOKING DOWN ON A SMALL SILVER MOTH, CAUGHT IN THE
BEAM OF A FLASHLIGHT.

---

### How the Code Works

The repository contains both exploratory “working out” code and the final decryption logic.

- **Exploratory stage:**  
  - Apply the Kasiski test by finding recurring substrings.  
  - Print them in order of frequency.  
  - Attempt simple substitutions to check for readable text.  
  - Used **Colorama** to style guessed substitutions and highlight undeciphered text for easier tracking.

- **Final stage:**  
  - Use the identified 17-character keyword to perform the actual Vigenère decryption.  
  - Each ciphertext letter is shifted backwards according to the corresponding key letter.

- **Frequency analysis:**  
  - Implemented in `frequency.py`.  
  - Splits ciphertext into 17 columns (based on key length).  
  - Tests candidate shifts per column and counts frequencies.  
  - Generates bar plots for each offset, saved under the `frequencies/` folder.  
  - Plots were compared against English frequency distributions to deduce correct key characters.

---

### How to Run

**Requirements:**  
- Python ≥ 3.6  

**Installation:**
```bash
pip install -r requirements.txt
```

If `pip` is not installed:

```bash
python -m ensurepip --upgrade
# or
python -m get-pip
```

**Running the code:**

- Run the deciphering logic:
```bash
python i_crack_vigeneres.py
```

- Produce frequency offset graphs:
```bash
python frequency.py
````
