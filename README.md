# Exercise: process safety

## Dpressurization of closed volume of ideal gas with heat input
Assume you have a volume of 20 m<sup>3</sup> with an ideal at 200 barg pressure. 

You can assume choked flow for your calculation.

m = CAP*sqrt((kM/ZRT)(2/(k+1))^(k+1)/(k-1))

You can use the following parameters: 

- R = 8.314 J/K mol
- C = 0.72
- k = c_p/c_v = 1.4
- Z = 1
- M = 25 g/mol
- T = 400 K
- C_v = 27 J/K mol 

You can assume a heat input of Q = 15kW, and that the volume is closed, except for blowdown. 

What diameter D must the blowdown orifice have in order to avoid rupture with more than 100 kg gas in the tank?

You can assume the tensile strength of the steel in the tank is given by 

P_y = 7E7 - 50000*(T-400)

measured in Pa.

## Equalization pressure over a compressor segment
Consider the case where you have a compressor unit operating 
at 10 barg suction pressure and 50 barg downstream pressure. 
The system is designed to operate at 80% of design pressure 
at the downstream side, and design pressure on the suction side 
is 25 barg.

Upstream of the compressor you have a cooler with internal hot side 
volume of 2 m3. You also have a scrubber with a volume of 5m3. 
The compressor house has a volume of 3 m3. Downstream piping 
including surge protection line holds 1 m3, and so does the 
upstream piping from isolation valve down to the compressor house.

Calculate the settle-out pressure at operating and design 
conditions. Will the upstream piping be overpressurized?

Would you use design conditions or operating conditions as 
basis for your process safety calculations?

## Solution
Clone the repository, then run `pip install -r requirements.txt`. It is recommended to use a virtual environment to avoid polluting the dependency space.

To solve the first, run the *blowdown.py* script as follows 

`./blowdown.py <diameter-in-mm> <tmax>`.

Vary the diameter until you find a suitable size.

To solve the second, simply run ./settleout.py.
