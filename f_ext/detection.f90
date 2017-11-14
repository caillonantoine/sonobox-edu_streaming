subroutine detection(x,y,search,amplitude,N)
implicit none

integer, intent(in) :: N,search
real, intent(in), dimension(N) :: x
integer, intent(out), dimension(N) ::y
real, intent(in) :: amplitude

integer, dimension(search) :: sparse,state
integer :: mm,nn,i,o
real :: step,thresh

step = amplitude/search

do mm=1,search
    state(mm) = 0
    sparse(mm) = 0
enddo

do mm=1,N
    do nn=1,search
        if (x(mm) < nn*step .and. state(nn) == 1) then
            sparse(nn) = sparse(nn) + 1
            state(nn) = 0
        elseif (x(mm) >= nn*step .and. state(nn) == 0) then
            sparse(nn) = sparse(nn) + 1
            state(nn) = 1
        endif
    enddo
enddo

thresh = maxloc(sparse,1)*step
i = 0
o = 0

do mm=1,N
    if (x(mm) >= thresh) then
        y(mm) = 1
    else
        y(mm) = 0
    endif
enddo

end subroutine detection




























