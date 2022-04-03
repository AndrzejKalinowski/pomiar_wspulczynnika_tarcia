# pomiar wspólczynnika tarcia

****
Eksperyment z pomiarem wspulczynnika tarcia (na fizyke).

This device uses an imu (mpu6050), a distance sensor (vl53l0x) and a peace of wood to calculate friction coefficient. An arduino reads the sensors values and sends it over serial port to the python program. Then the data is then interpreted and simplee trig is used to calculate the coefficient. 
