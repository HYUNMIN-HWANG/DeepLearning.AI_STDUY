t = [0:0.01:0.98]
y1 = sin(2*pi*4*t)
plot(t, y1) 

y2 = cos(2*pi*4*t)

hold on;        % 두 개 동시에 plot할 수 있음
plot(t, y2, 'r')    
xlabel('time')  % x축 라벨
ylabel('value') % y축 라벨
legend('sin','cos')
title('my plot')
print -dpng 'myPlot.png'    % 이미지 저장
close

figure(1) ; plot(t, y1)
figure(2) ; plot(t, y2)


subplot(1,2,1) ; % Divides plot a 1X2 grid, access first element
plot(t, y1)
subplot(1,2,2)
plot(t, y2)
% x축, y축
axis([0.5 1 -1 1])


clf;

A = magic(5)
imagesc(A)
imagesc(A), colorbar, colormap gray;
