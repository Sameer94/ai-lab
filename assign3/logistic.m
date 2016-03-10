#logistic regression -gradient desecnt

[a1,a2,y]=textread("ex2data2.txt","%f,%f,%f");
N=length(y);
count=0;
x1=[a1,a2];
wln=3;
w(1:wln)=rand; 
n=0.1;

for i=1:N

    if y(i)==0
    y(i)=-1;
    end
z(i)=1;    
end

for k=1:118
f=(w(1)*z')+(w(2).*a1)+(w(3).*a2);
h=1/(1+exp(-f));

ew1=(h'-y);

e=(h'-y)'*(exp(f)/(1+exp(f)).^2)*x1();

w(1)=w(1)-(n*sum(ew1))/N;

for i=2:wln
	w(i)=w(i)-(n*e(i-1))/N;

end
#plot(k,e(1)+e(2));
#plot(a1(k),a2(k),h ,'r');
#hold on;

end
p=[z',a1,a2];
plotData(p(:,2:3),y);
hold on;

n=-1:0.1:1;
m=-(w(1)/w(3))-(w(1)/w(3))*n;
plot(n,m);

