dt        =20
idt_emis_s=207
idt_emis_e=208
i_emis    =20
j_emis    =17
t_emis    =69
t_eva     =71
minutes_emis_to_evaluation   =2
emis_rate =118.8
dx        =2000
iZ        =27
RE        =1
agi_r     =1.69e-05
FirstTime =0
;===============================================================================;
;---calculate some variable---
  rho_agi          = 5.683                   ;Density of AgI particle (g cm-3)
  PI               = 3.1415926536            ;pi
  v_agi            = (4/3)*PI*(agi_r)^3      ;Mean volume of AgI particle (cm-3)
print((4*PI*(agi_r)^3/3))
print(PI*(agi_r)^3)
print((4/3)*PI*(agi_r)^3)
print((4./3)*PI*(agi_r)^3)
  m_agi            = 1.e6*rho_agi*v_agi      ;Mean mass of AgI particle (ug)
  area             = dx*dx ;m2
  e_m              = emis_rate*dt*(idt_emis_e-idt_emis_s+1)/1000000.0 ;ug -> g
  e_m              := area*e_m
  e_n              = emis_rate*dt*(idt_emis_e-idt_emis_s+1)/m_agi   ; ug - n
  e_n              := area*e_n
  e_nm             = e_n/e_m






print(e_nm)
