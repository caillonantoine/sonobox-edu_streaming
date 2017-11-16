subroutine detection(x,y,N)
implicit none

integer, intent(in) :: N
real, intent(in), dimension(N) :: x
integer, intent(out), dimension(20) :: y

integer :: i,o,k,f,m,nb
real :: t

i = 0
o = 0
nb = 1

do k=1,10
    t = 1 - real(k)/10
    do m=1,N
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

!def detection(array):
!    freq = []
!    i = 0
!    o = 0
!    for k in range(10):
!        t = 1 - k/10.
!        for ind,val in enumerate(array):
!            if val >= t and i == 0:
!                i = ind
!            elif val < t and i != 0:
!                o = ind
!            
!            if i != 0 and o != 0:
!                mes = np.argmax(array[i:o]) + i
!                if mes in freq:
!                    i,o = 0,0
!                else:
!                    freq.append(mes)
!                    i,o = 0,0
!    return freq

end subroutine detection