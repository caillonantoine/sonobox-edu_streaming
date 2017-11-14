subroutine detection(x,y,search,amplitude,N)
implicit none

integer, intent(in) :: N,search
real, intent(in), dimension(N) :: x
real, intent(out), dimension(N) ::y
real, intent(in) :: amplitude

integer, dimension(search) :: sparse,state
integer :: ii,jj
real :: step

step = amplitude/search

do ii=1,N
	do jj=1,search
		if x(ii) < jj*step .and. state(jj) == 1 then
			sparse(jj) = sparse(jj) + 1
			state(jj) = 0
		elseif x(ii) > jj*step .and. state(jj) == 0 then
			sparse(jj) = sparse(jj) + 1
			state(jj) = 1
		endif
	enddo
enddo

y = maxloc(sparse)*step
			

end subroutine detection
