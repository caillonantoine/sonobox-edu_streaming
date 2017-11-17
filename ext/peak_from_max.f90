subroutine detection(x,y,N)
implicit none

!Dans ce programme, on va diviser l'axe vertical du spectre en 10 morceaux et effectuer une
!recherche de pics sur ces 10 morceaux.
!Dès qu'on découvre un nouveau pic sur un des 10 morceaux, on le repertorie dans un tableau.


integer, intent(in) :: N !taille de X
real, intent(in), dimension(N) :: x !donnée audio d'entrée
integer, intent(out), dimension(20) :: y !tableau de fréquences

integer :: i,o,k,f,m,nb !in point,out point,vars muettes
real :: t !threshold

i = 0
o = 0
nb = 1

do k=1,10 !division du spectre
    t = 1 - real(k)/10 !initialisation du threshold
    do m=1,N !recherche de pics
        if (x(m) >= t .and. i == 0) then
            i = m
        elseif (x(m) < t .and. i /= 0) then
            o = m
        endif
        if (i /= 0 .and. o /= 0) then
            f = maxloc(x(i:o),1) + i - 2
            if (any(y==f)) then
                i = 0
                o = 0
            else
                y(nb) = f
                i = 0
                o = 0
                nb = nb +1
            endif
        endif
    enddo
enddo
end subroutine detection