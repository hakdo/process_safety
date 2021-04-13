###############################################################
# blowdown.py
#
# Script to calculate settle-oput pressure.
# Usage: ./settleout.py
#
# Dependencies: none.
# H. Olsen - 2021 @sjefersuper
# License: MIT
###############################################################

# Physical constants and parameters
p1ops = 10.
p2ops = 50.
p1design = 25.

# Upstream volume - up to compressor house
V1 = 2. + 5. + 1. # cooler, scrubber, piping
V2 = 3. + 1. #compressor house, piping

def settle(p1,V1,p2,V2):
    pso = (p1*V1 + p2*V2)/(V1+V2)
    return pso

if __name__ == "__main__":
    print("Design pressure suction side: ", p1design)
    print("Design pressure downstream side: ", p2ops/0.8)
    pso_design = settle(p1design, V1, p2ops/0.8, V2)
    print("Settle-out from design conditions: ", pso_design)
    pso_ops = settle(p1ops, V1, p2ops, V2)
    print("Settle-out from process steady-state conditions: ", pso_ops)
